# -*- coding: utf-8 -*-
from base_request_handler import JsonRequestHandler
from lx_decorators.decorator import rate_limit


class MainHandler(JsonRequestHandler):

    @rate_limit(1)
    def get(self):
        print(self.request.uri)
        self.write({'dad':"Hello, world"})
