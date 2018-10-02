#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import signal
import logging
import logging.config
import MySQLdb

# setup the log
logging.config.fileConfig("logging.conf")
LOG = logging.getLogger()


LOG.info("###### NEW INSTANCE #####")
LOG.log(51, "Current level is: {0}".format(logging.getLevelName(LOG.getEffectiveLevel())))

# the gpio pin, the rain gauge is connected to
# see column BCM of 'gpio readall'
PIN = 15

DB_USER = "therck"
DB_SERVER = "cerban.local"
DB_DATABASE = "raingauge"
DB_TABLE = "data"
DB_SENSOR_ID = "1"


LOG.info("setting up GPIO")
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def cb(channel):
    LOG.debug("callback from channel {0}".format(channel))
    try:
        connection = MySQLdb.connect(DB_SERVER, DB_USER, "", DB_DATABASE)
        cursor = connection.cursor()
        query = "INSERT INTO {0} (sensor_id) VALUES ({1})".format(DB_TABLE, DB_SENSOR_ID)
        cursor.execute(query)
        connection.commit()
    except MySQLdb.OperationalError as e:
        LOG.error("MySQL Connection Error: {0}".format(e))
    finally:
        connection.close()


GPIO.add_event_detect(PIN, GPIO.RISING, callback=cb, bouncetime=500)

LOG.info("registered callback")

def sigkill(signum, frame):
    LOG.info("received SIGTERM")

signal.signal(signal.SIGTERM, sigkill)

# wait for any signal before ending the program
try:
    signal.pause()
except KeyboardInterrupt:
    LOG.info("catched keyboard interrupt")

LOG.info("terminated")
