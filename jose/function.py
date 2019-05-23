# def say_hello(name = "NAME"):
#     print "hello " + name
# say_hello()

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def add(n1,n2):
#     return n1+n2

# result = add(20,30)
# print result

#ARGS(TUPLE)

# def myfunc(*args):
#     print sum(args) * 0.05

# myfunc(40,20,100,40)

# def myfunc(*args):
#     for item in args:
#         print(item)
# myfunc(40,20,100,60,80)

#KWARGS(DICTIONARY)

# def myfunc(**kwargs):
#     print kwargs
#     if 'fruit' in kwargs:
#         print 'My fruit of choice is '+kwargs['fruit']
#     else:
#         print 'I did not find any fruit here'
        
# myfunc(fruit='apple',veggie='lettuce')

x=10
formatted = f("I've told you {x} times already!")
print (formatted)