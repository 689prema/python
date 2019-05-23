#Higher Order

# def sum(n,func):
#     total = 0
#     for num in range(1,n+1):
#         total += func(num)
#     return total

# def square(x):
#     return x*x
    
# def cube(x):
#     return x*x*x
    

# print(sum(3,cube))
# print(sum(3,square))

# from random import choice

# def greet(person):
#     def get_mood():
#         msg = choice(('Hello there','Go away','I love you'))
#         return msg
    
#     result = get_mood() + person
#     return result

# print(greet("Tobby"))

#####  DECORATOR #######

# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper
    
# @be_polite
# def greet():
#     print("My name is Prema.")
    
# @be_polite
# def rage():
#     print("I HATE YOU!")
    
# greet()
# rage()
    
## greet = be_polite(greet)
# #polite_rage = be_polite(rage)
# #polite_rage()

