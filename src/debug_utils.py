
from __future__ import print_function

DEBUG_PRINT_ENABLED_ = False

def debug_print(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        if DEBUG_PRINT_ENABLED_:
            print('enter: ' + func_name)
        res = func(*args, **kwargs)
        if DEBUG_PRINT_ENABLED_:
            print('exit: ' + func_name)
        return res
    return wrapper

"""
Test
"""
"""
@debug_print
def hello():
    print('hello')

hello()
"""
