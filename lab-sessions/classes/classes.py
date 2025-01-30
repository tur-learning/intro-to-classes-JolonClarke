#class Person: # Classwork
#    def __init__(self, name, age, height):
#        self.name = name
#        self.age = age
#        self.height = height
    
#    def info(self):
#        print(self.name, self.age, self.height)

#    def change_age(self, new_age):
#        self.age = new_age

#----------------------------------------------------------------------------
# Assignment:
   
class Chip:
    def __init__(self, flavor, texture, size, brand):
        self.flavor = flavor
        self.texture = texture
        self.size = size # in cm
        self.brand = brand

    def info(self):
        print(self.flavor, self.texture, self.size, self.brand)

    def change_brand(self, new_brand):
        self.brand = new_brand
    
    def chips_length(self): # how many centimeters if all chips in a bag are laid in a line
        bag_length = self.size * 24 # the median number of chips per bag, according to Google
        print(str(bag_length) + " cm")