class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def __repr__(self):
        return "{} is a {}".format(self.name,self.species)
        
    def make_sound(self, sound):
        print("this animal says {}".format(sound))
        
    
class Cat(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,species="Cat")
        #super().__init__(name,species)
        #Animal.__init__(self,name,species)
        self.breed = breed
        self.toy = toy
        
    def play(self):
        print("{} play with {}".format(self.name,self.toy))

#blue = Cat("Blue","Cat","Scottish Fold","String")
blue = Cat("Blue","Scottish Fold","String")
print(blue)
print(blue.species)
print(blue.breed)
print(blue.toy)
blue.play()