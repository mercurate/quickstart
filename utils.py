#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def benchmark(func):
    """
    A decorator that print the time of function take
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper
 
 
def loggin(func) :
    """
    A decorator that logs the activty of the script.
    Ok, it really just print it, put it could be loggin !
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper
 
 
def counter(func):
    """
    A decorator that print the number of time a function has been executed
    """
    counter.count = 0
    def wrapper(*args, **kwargs):
        counter.count = counter.count + 1
        res = func(*args, **kwargs)
        print func.__name__, "has been used : ", counter.count, "X"
        return res
    return wrapper

