import os
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
certfile="fullchain.pem"
keyfile="privkey.pem"
