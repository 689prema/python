# from random import random

# def flip_coin():
#     r=random()
#     if r>0.5:
#         return "Heads"
#     else:
#         return "Tails"
# #print(flip_coin())

# def flip_coin():
#     if random() > 0.5:
#         return "HEADS"
#     else:
#         return "TAILS"
# print(flip_coin())

#Function with parameter

# def divide(num1, num2):
#     return num1/num2
    
# print(divide(2,5))
# print(divide(5,2))

#*ARGS
# def sum_all_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(sum_all_nums(4,6,9,4,10))
# print(sum_all_nums(4,6))

#**KWARGS

# def fav_colors(**kwargs):
#     for person,color in kwargs.items():
#         print("{}'s favorite color is {}".format(person,color))
# fav_colors(colt="purple",ruby="red",ethel="teal")
# fav_colors(colt="purple",ruby="red",ethel="teal",ted="green")
# fav_colors(colt="royal deep amazing purple")

# #Parameter Ordering
# 1.Parameters
# 2.*args
# 3.default parameters
# 4.**kwargs
