@echo off
title "Configuring windows variables for the Flask APP"

set FLASK_APP=app.py
echo FLASK_APP value set to %FLASK_APP%
set DATABASE_URL=postgresql://postgres:WFwt8UDpkfUpRsVS@localhost/dev
echo DATABASE_URL value set to %DATABASE_URL%
set DEVTEST_CONF=DEVEL
echo DEVTEST_CONF value set to %DEVTEST_CONF%
set IP_ADDRESS=127.0.0.1
echo IP_ADDRESS value set to %IP_ADDRESS%
set PORT=5001
echo PORT value set to %PORT%

nose2 -v