ps aux | grep runcpserver |grep 8088| cut -c 9-15 | xargs kill
su www-data -c "ENV/bin/python ./manage.py runcpserver host=0.0.0.0 port=8088&"
