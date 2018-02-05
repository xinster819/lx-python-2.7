#coding=utf8

# uwsgi --http :9090 --wsgi-file foobar.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
# --http 端口  --wsgi-file 启动文件
"""
uwsgi每次启动， 除了processes参数指定的进程以外， 还会启动master进程负责管理其他进程， http进程负责端口监控

"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b'hello world']