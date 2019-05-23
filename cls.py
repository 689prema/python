# class User:
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
    
# user1 = User("Joe","Smith",68)
# user2 = User("Blanca","Lopez",41)
# print(user1.first, user1.last)
# print(user2.first,user2.last)

# class Person:
#     def __init__(self):
#         self.name = "Tony"
#         self._secret = "hi!"
#         self.__msg = "I like turtles!"
#         self.__lol = "HaHAHAHA"

# p= Person()

# print(p.name)
# print(p._secret)
# print(dir(p))
# print(p._Person__msg)
# print(p._Person__lol)

#Adding Instance Method

# class User:
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
    
#     def full_name(self):
#         return "{} {}".format(self.first,self.last)
    
#     def initials(self):
#         return "{}.{}".format(self.first[0],self.last[0])
        
#     def likes(self,thing):
#         return "{} likes {}".format(self.first,thing)
        
#     def is_senior(self):
#         return self.age >= 65
        
#     def birthday(self):
#         self.age += 1
#         return "Happy {}th, {}".format(self.age,self.first)
        
# user1 = User("Joe","Smith",68)
# user2 = User("Blanca","Lopez",41)

# # print(user2.full_name())
# # print(user1.likes("Ice Cream"))
# # print(user2.likes("Chips"))

# # print(user2.initials())
# # print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

#Class Attributes


class User:
    
    active_users = 0
    
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
    def logout(self):
        User.active_users -=1
        return "{} has logged out".format(self.first)
    
    def full_name(self):
        return "{} {}".format(self.first,self.last)
    
    def initials(self):
        return "{}.{}".format(self.first[0],self.last[0])
        
    def likes(self,thing):
        return "{} likes {}".format(self.first,thing)
        
    def is_senior(self):
        return self.age >= 65
        
    def birthday(self):
        self.age += 1
        return "Happy {}th, {}".format(self.age,self.first)
        
print(User.active_users)
user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",41)
print(User.active_users)
print(user2.logout())
print(User.active_users)


