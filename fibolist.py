#!/usr/bin/env python

import math

n = raw_input('please a num: ')

def func(x):
    '''a = math.sqrt(5)
    b = 1 + a
    c = 1 - a
    d = (b/2) **x
    e = (c/2) **x
    f = 1/a*(d-e)'''
    fn = 1/math.sqrt(5)*(((1+math.sqrt(5))/2)**x-((1-math.sqrt(5))/2)**x)
    print int(fn)

def func1(x1):
    '''
    if x1 < 3:
        fn = 1
        return fn
    else:
        return (func1(x1-1) + func1(x1-2))
    '''
    return (1 if x1 < 3 else (func1(x1-1)+func1(x1-2)))

if __name__ == '__main__':
    func(int(n))
    print func1(int(n))

