ps aux | grep runcpserver | grep 8088 | cut -c 9-15 | xargs kill
