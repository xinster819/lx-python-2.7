# -*- coding: utf-8 -*-

class old_style_c:
    a = 1

class new_style_c(object):
    b = 1


o = old_style_c()
n = new_style_c()
print(type(o), o.__class__)
print(type(n), n.__class__)


class A(object):
    pass

class B(object):
    pass


class X(A, B):
    pass

class Y(A, B):
    pass


class Z(X, Y):
    pass

z = Z()

print(Z.__mro__)

class First(object):
    def __init__(self):
        print "first"

class Second(object):
    def __init__(self):
        print "second"

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print "that's it"


t = Third()

a_var = 'global value'

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()
    print

outer()