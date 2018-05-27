@echo off
title "Configuring windows variables for the Flask migration tool"

set FLASK_APP=app.py
echo FLASK_APP value set to %FLASK_APP%
set DATABASE_URL=postgresql://postgres:WFwt8UDpkfUpRsVS@localhost/dev
echo DATABASE_URL value set to %DATABASE_URL%
set DEVTEST_CONF=DEVEL
echo DEVTEST_CONF value set to %DEVTEST_CONF%

python manage.py db init