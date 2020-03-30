import os
import time
pidfile = 'app01.pid'
worker_tmp_dir = '/dev/shm'
worker_class = 'gthread'
workers = 8
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 4
proc_name = 'app01'
bind = '0.0.0.0:443'#+ str(os.environ["port_addr"])
backlog = 2048
accesslog = '-'
errorlog = '-'
loglevel='debug'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
certfile="/tmp/fullchain.pem"
keyfile="/tmp/privkey.pem"
errorlog = '/tmp/errorfile'
capture_output = True
