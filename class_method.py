class User:
    
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return "There are currently {} active users".format(cls.active_users)
        
    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))
    
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
        
class Moderator(User):
    total_mods = 0
    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_mods += 1
        
    @classmethod
    def display_active_mods(cls):
        return "There are currently {} active mods".format(cls.total_mods)
        
    def remove_post(self):
        return "{} removed a post from the {} community".format(self.full_name(),self.community)
        
# user1 = User("Joe","smith",68)
# user2 = User("Blanca","Lopez",41)
# print(User.display_active_users())

# user1 = User("Joe","smith",68)
# user2 = User("Blanca","Lopez",41)
# print(User.display_active_users())

# tom=User.from_string("Tom,Jones,89")
# print(tom.first)
# print(tom.full_name())
# print(tom.birthday())

# jasmine = Moderator("Jasmine","O'conner",61,'Piano')
# print(jasmine.full_name())
# print(jasmine.community)

# print(User.display_active_users())
# u1 = User("Tom","Garcia",35)
# print(User.display_active_users())
# jasmine = Moderator("Jasmine","O'conner",61,'Piano')
# print(User.display_active_users())

u1 = User("Tom","Garcia",35)
u2 = User("Tom","Garcia",35)
u2 = User("Tom","Garcia",35)
jasmine = Moderator("Jasmine","O'conner",61,'Piano')
jasmine2 = Moderator("Jasmine","O'cornner",61,'Piano')
print(User.display_active_users())
print(Moderator.display_active_mods())