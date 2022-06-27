# Raingauge

Collect input from a rain gauge and write it to a database.


## Requirements

`libmariadb-dev-compat` on Debian 9


## Install Service

    install raingauge.service /lib/systemd/system/

    # first install
    systemctl enable raingauge.service

    # already installed
    systemctl daemon-reload

    systemctl start raingauge.service
