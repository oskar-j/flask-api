@echo off
title Configuring windows variables for the Flask APP
set FLASK_APP=app.py
echo FLASK_APP value set
set DATABASE_URL=postgresql://postgres:WFwt8UDpkfUpRsVS@localhost/dev
echo DATABASE_URL value set
set DEVTEST_CONF=..\conf\dev_config.py
echo DEVTEST_CONF value set
flask run