update log:

20111104:
* add this to .py top:
#!/usr/bin/env python
# -*- coding: utf-8 -*-

* add clean.py, clean no use files

* change time zone:
TIME_ZONE = 'Asia/Shanghai'

* add HERE setting, it's useful:
HERE = os.path.dirname(os.path.abspath(__file__))

* ADMINS default to me:
ADMINS = (
    ('mercurate', 'mercurate@163.com'),
)

* use sqlite3 by default

* enable admin by default

* add localsettings import and localsettings.py.example
# custom settings
from localsettings import *

* make ./templates default in settings

* chmod a+x manage.py

* add default HOST:
HOST = 'http://0.0.0.0:8088'
