# -*- coding: utf-8 -*-
import time

from tornado import escape
from tornado.web import RequestHandler
from tornado.escape import utf8



class JsonRequestHandler(RequestHandler):


    def prepare(self):
        self.start = time.time()

    def write(self, chunk):
        """
        严格限制只返回json
        """
        if self._finished:
            raise RuntimeError("Cannot write() after finish()")
        if not isinstance(chunk, dict):
            raise RuntimeError("response not json format")
        chunk = escape.json_encode(chunk)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)


    def on_finish(self):
        print(time.time() - self.start, self.get_status())