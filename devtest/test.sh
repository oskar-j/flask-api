#!/bin/bash

echo "Configuring windows variables for the Flask APP"

export FLASK_APP=app.py
echo FLASK_APP value set to $FLASK_APP

export DATABASE_URL=postgresql://dev:WFwt8UDpkfUpRsVS@localhost/dev
echo DATABASE_URL value set to $DATABASE_URL

export DEVTEST_CONF=DEVEL
echo DEVTEST_CONF value set to $DEVTEST_CONF

export IP_ADDRESS=127.0.0.1
echo IP_ADDRESS value set to $IP_ADDRESS

export PORT=5001
echo PORT value set to $PORT

nose2 -v