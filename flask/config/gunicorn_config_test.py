import os
from config.model_config import *

bind = f"0.0.0.0:{port}"
workers = 2
threads = 2

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# backlog = 2048
preload_app = False # 使用pytorch 设置成True 会报错 https://blog.csdn.net/Ang_Quantum/article/details/122496024
# worker_class = "gevent"
# worker_connections = 1000
# daemon = False #后台运行,默认False
timeout = 120

if not os.path.exists(basedir+'/log'):
    os.mkdir(basedir+'/log')
pidfile = os.path.join(basedir, 'log/gunicorn.pid')
accesslog = os.path.join(basedir, 'log/access.log')
errorlog = os.path.join(basedir, 'log/gunicorn.log')
