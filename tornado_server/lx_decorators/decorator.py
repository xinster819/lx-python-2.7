# -*- coding: utf-8 -*-
import time

limit_rate = {}

def rate_limit(rate=0):
    def _decorator(func):
        def func_wrapper(self):
            try:
                uri = self.request.uri
                if not uri:
                    pass
                if _rate_limit(rate, uri):
                    {'dad':"Hello, wofffrld"}
                else:
                    func(self)
            except Exception as e:
                import traceback
                traceback.print_exc()
        return func_wrapper
    return _decorator

def _rate_limit(rate, uri):
    print(limit_rate.get(uri, 0))
    is_limit = False
    if rate == 0:
        return is_limit

    if limit_rate.get(uri, 0) > rate:
        is_limit = True
    limit_rate[uri] = limit_rate.get(uri, 0) + 1

    return is_limit