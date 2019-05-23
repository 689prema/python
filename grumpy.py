class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self,key):
        print("YOU CANT {}? WELL IT AINT HERE!".format(key))
        
    def __setitem__(self,key,value):
        print("You want to change the dictionary?")
        print("Ok fine..")
        super().__setitem__(key,value)
        
    def __contains__(self,item):
        print("NO IT AINT IN HERE!")
        return False
        
data = GrumpyDict({"first":"Tom","animal":"cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
'city' in data