# -*- coding: utf-8 -*-
from utils.lru import LRU_CACHE, LRU_LIMIT


_cache = LRU_LIMIT(2, 3)

def rate_limit(rate=0):
    def _decorator(func):
        def func_wrapper(self):
            try:
                uri = self.request.uri
                if not uri:
                    pass
                if _cache.incr(uri, 1) > 2:
                    print(_cache.get(uri).v)
                    self.write({'ddd':'dee'})
                else:
                    func(self)
            except Exception as e:
                import traceback
                traceback.print_exc()
        return func_wrapper
    return _decorator