# -*- coding: utf-8 -*-
from linked_list import DoublyLinkedList, ExpireDoublyLinkedEntry

class LRU_CACHE():
    r'''
    not thread safe
    '''


    def __init__(self, count=32, expire_millis=-1):
        self.count = count
        self.cache = {}
        self.expire_millis = expire_millis
        self._list = DoublyLinkedList()

    def put(self, k, v):
        node = self.get(k)
        if node:
            node.update(v)
            self._list.remove(node)
        else:
            node = ExpireDoublyLinkedEntry(k, v, self.expire_millis)
            if self.isfull():
                self.clean()
            self.cache[k] = node
        self._list.insert_beginning(node)

    def incr(self, k, count):
        node = self.get(k)
        if node:
            node.incr(count)
        node = ExpireDoublyLinkedEntry(k, 1, self.expire_millis)
        if self.isfull():
            self.clean()
        self.cache[k] = node
        self._list.insert_beginning(node)

    def isfull(self):
        return len(self.cache) >= self.count

    def clean(self):
        while self.isfull() or self._list.tail.is_expire():
            self.remove(self._list.tail.k)

    def get(self, k, default=None):
        if k not in self.cache:
            return default

        if self.cache.get(k).is_expire():
            self.remove(k)
            return default
        return self.cache.get(k)

    def remove(self, k):
        # not thread-safe
        v = self.cache.pop(k)
        if v:
            self._list.remove(v)

    def clear_list(self):
        self._list.remove_last()


class LRU_LIMIT():
    r'''
    not thread safe
    '''
    def __init__(self, count=32, expire_millis=-1):
        if expire_millis <= 0:
            raise Exception
        self.count = count
        self.cache = {}
        self.expire_millis = expire_millis
        self._list = DoublyLinkedList()

    def put(self, k, v):
        node = self.get(k)
        if node:
            node.update(v)
        else:
            node = ExpireDoublyLinkedEntry(k, v, self.expire_millis)
            self.clean()
            self.cache[k] = node
            self._list.insert_beginning(node)

    def incr(self, k, count):
        node = self.get(k)
        if node:
            node.incr(count)
        else:
            node = ExpireDoublyLinkedEntry(k, 1, self.expire_millis)
            self.clean()
            self.cache[k] = node
            self._list.insert_beginning(node)

        return self.get(k).v

    def isfull(self):
        return len(self.cache) >= self.count

    def clean(self):
        if self.isfull():
            while self.isfull() or self._list.tail.is_expire():
                self.remove(self._list.tail.k)

    def get(self, k, default=None):
        if k not in self.cache:
            return default
        if self.cache.get(k).is_expire():
            self.remove(k)
            return default
        return self.cache.get(k)

    def remove(self, k):
        v = self.cache.pop(k)
        if v:
            self._list.remove(v)

    def clear_list(self):
        self._list.remove_last()
