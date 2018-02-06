# -*- coding: utf-8 -*-
from time import time


class ExpireDoublyLinkedEntry(object):

    r'''
    数据缓存
    '''

    def __init__(self, k, v, milliseconds, prev=None, next=None, auto_update_expire=False):
        self.k = k
        self.v = v
        self.milliseconds = milliseconds
        self.prev = prev
        self.next = next
        self.update_expire()
        self.auto_update_expire = auto_update_expire

    def is_expire(self):

        print(time(), self.expire, True if (time() > self.expire) else False)
        return True if (self.expire > 0 and time() > self.expire) else False

    def update_expire(self):
        self.expire = -1 if self.milliseconds <= 0 else (time() + self.milliseconds)

    def update(self, v):
        self.v = v
        if self.auto_update_expire:
            self.update_expire()

    def incr(self, count):
        try:
            self.v = int(self.v) + count
        except Exception:
            raise Exception

    def reset(self):
        self.prev = None
        self.next = None


class DoublyLinkedList(object):

    head = None
    tail = None

    def insert_beginning(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insert_before(node, self.head)

    def insert_before(self, new_node, node):
        new_node.next = node
        if node.prev is None:
            self.head = new_node
        else:
            node.prev.next = new_node
            new_node.prev = node.prev
        node.prev = new_node

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.reset()


    def remove_last(self):
        if not self.tail:
            return
        self.remove(self, self.tail)