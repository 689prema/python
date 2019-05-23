class Aquatic:
    def __init__(self,name):
        print("Aquatic")
        self.name = name
    
    def swim(self):
        return "{} is swimming".format(self.name)
        
    def greet(self):
        return "I am {} of the sea!".format(self.name)

class Ambulatory:
    def __init__(self,name):
        print("Ambulatory")
        self.name = name
    
    def walk(self):
        return "{} is walking".format(self.name)
    
    def greet(self):
        return "I am {} of the land!".format(self.name)
        
class Penguin(Ambulatory,Aquatic):
    def __init__(self,name):
        print("PENGUIN")
        Ambulatory.__init__(self,name=name)
        Aquatic.__init__(self, name=name)
        
captain_cook = Penguin("Captain Cook")
print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())