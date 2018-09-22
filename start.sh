#!/bin/bash

PIDFILE="/run/user/$UID/raingauge.pid"

# check whether pidfile exists and start program
if ! [ -e $PIDFILE ]; then
    ./raingauge.py &
    echo $! > $PIDFILE
else
    echo "Pidfile exists. Nothing to do..."
fi
