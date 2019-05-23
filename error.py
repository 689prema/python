# def colorize(text,color):
#     colors =("cyan","yellow","blue","green","magenta")
#     if type(color) is not str:
#         raise TypeError("color must be instance of str")
#     if type(text) is not str:
#         raise TypeError("text must be instance of str")
#     if color not in colors:
#         raise ValueError("color is invalid color")
#     print("Printed {} in {}".format(text,color))

# colorize("Hello","yellow")

#TRY AND EXCEPT

# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")

# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return None
# d= {"name":"Ricky"}
# print(get(d,"name"))
# print(get(d,"city"))

#Try,except,else,finally

# try:
#     num = int(input("please enter a number:"))
# except:
#     print("That's not a number!")
# else:
#     print("I'M IN THE ELSE")
# finally:
#     print("RUNS NO MATTER WHAT!")

# while True:
#     try:
#       num = int(input("please enter a number:"))
#     except ValueError:
#       print("That's not a number!")
#     else:
#       print("Good job, you entered a number!")
#       break
#     finally:
#       print("RUNS NO MATTER WHAT!")

# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("don't divide by zero please. . .")
#     except TypeError as err:
#         print("a and b must be ints or floats")
#         print(err)
#     else:
#         print("{} divided by {} is {}".format(a,b,result))
# def divide(a,b):
#     try:
#         result = a/b
#     except (ZeroDivisionError,TypeError) as err:
#         print("Something went wrong!")
#         print(err)
#     else:
#         print("{} divided by {} is {}".format(a,b,result))


# print(divide(1,2))
# print(divide(1,0))

#Debugging PDB # type l - list of content
# import pdb
# first="First"
# second="Second"
# pdb.set_trace()
# result = first +second
# third = "Third"
# result += third
# print(result)

def add_numbers(a,b,c,d):
    import pdb; pdb.set_trace()
    return a + b + c + d
    
add_numbers(1,2,3,4)