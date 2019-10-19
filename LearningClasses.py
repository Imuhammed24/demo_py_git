class Animal():
    name = "Bird"
    noise = "Shriek"
    size = "Small"
    color = "Brown"
    body = "Feather"

    def get_info(self):
        return self.name,self.color,self.size


Eagle = Animal() #creates an instance of class animal.
parrot = Animal() #creates an instance of class animal.
Dove = Animal() #creates an instance of class animal.
Dove.name ='Dove' #Gives object "Dove" a property.
Dove.color ='White' #Gives object "Dove" a property.


print("-name: %s \n-color: %s \n-size: %s" %(Dove.get_info()))
