#!/bin/bash

echo "Configuring windows variables for the Flask APP"

FLASK_APP=app.py
echo FLASK_APP value set to $FLASK_APP

DATABASE_URL=postgresql://dev:WFwt8UDpkfUpRsVS@localhost/dev
echo DATABASE_URL value set to $DATABASE_URL

DEVTEST_CONF=DEVEL
echo DEVTEST_CONF value set to $DEVTEST_CONF

IP_ADDRESS=127.0.0.1
echo IP_ADDRESS value set to $IP_ADDRESS

PORT=5001
echo PORT value set to $PORT

nose2 -v