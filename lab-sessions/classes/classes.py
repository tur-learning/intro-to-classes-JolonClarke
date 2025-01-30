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
   
class Chip: #potato chips
    def __init__(self, flavor, texture, length, brand):
        self.flavor = flavor # the flavor of the potato chips
        self.texture = texture # the texture of the chips (eg. smooth, rippled, etc...)
        self.length = length # length in cm
        self.brand = brand # who made the chips

    def info(self): # The line below explains what each attribute is
        print("The flavor is " + self.flavor + ", the chip texture is " + self.texture + ", the length of one chip is " + str(self.length) + " centimeters, and the brand of the chips is " + self.brand + ".")

    def change_brand(self, new_brand): # this allows you to change the brand of the chips (eg Lays, Doritos, Pringles...)
        self.brand = new_brand
    
    def chips_length(self): # how many centimeters if all pf the chips in a bag are laid in a line
        bag_length = self.length * 24 # the median number of chips per bag, according to Google
        print("If you laid all of the chips in that bag in a line, the line would be " + str(bag_length) + " centimeters long.")