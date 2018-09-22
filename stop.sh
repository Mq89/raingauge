#!/bin/bash

PIDFILE="/run/user/$UID/raingauge.pid"

if [ -e $PIDFILE ]; then
    kill $(< $PIDFILE)
    rm $PIDFILE
fi
