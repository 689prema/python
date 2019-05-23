# def shout(fn):
#     def wrapper(*args,**kwargs):
#         return fn(*args,**kwargs).upper()
#     return wrapper

# @shout
# def greet(name):
#     return "Hi, I'm {}".format(name)
    
# @shout
# def order(main,side):
#     return "Hi, I'd like the {}, with a side of {},please".format(main,side)

# @shout
# def lol():
#     return "lol"

# print(greet("todd"))
# print(order("burger","fries"))
# print(lol())

from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print("Time Elapsed: {}".format(end_time - start_time))
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(1000000))

print(sum_nums())