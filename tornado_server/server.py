# -*- coding: utf-8 -*-

import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from uri_paths import paths

import config


if __name__ == "__main__":
    application = tornado.web.Application(paths)

    sockets = tornado.netutil.bind_sockets(config.port, backlog=128)
    tornado.process.fork_processes(0)
    server = HTTPServer(application)
    server.add_sockets(sockets)

    tornado.ioloop.IOLoop.current().start()
