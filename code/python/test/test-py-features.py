#!/usr/bin/env python
#coding:utf8

class Test(object):

    def func1():
        pass

    def __getattr__(self, name):
        return '__getattr__(' + name + ')'

    def __setattr__(self, name, value):
        print('__setattr__(' + name + ', ' + str(value) + ')')

    def __delattr__(self, name, value):
        pass

def main():
    print("Hey guys. This is only a test for pythons\' coolest features.")
    t = Test()

    # __setattr__ couldn't assign to dict.
    # especially function doesn't have a dict access..
    # t.__dict__['a'] = "123";

    # call __setattr__ instead of normal set..
    t.x = 1

    # call __getattr__ if any attr cannot be get by the normal way.
    print(t.a)

if __name__ == '__main__':
    main()
