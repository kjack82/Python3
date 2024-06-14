## A class variable  is a variable that is the same for every instance of the class

class Musician:
  title = "Rockstar"  ##defining a class variable, must be indented 

drummer = Musician()
print(drummer.title)
# prints "Rockstar"

## if did 
guitarist = Musician()
##it would still have title attribute

### METHODS ######
# Methods are functions that are part of a class
# First arguement in a method is always the object calling the method 
# Recommended to call this self 

class Dog:  #class defined 
  dog_time_dilation = 7

  def time_explanation(self): #method created taking one arguement and refers to object calling the function 
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog() #created a dog named pip
pipi_pitbull.time_explanation() #called the method
# Prints "Dogs experience 7 years for every 1 human year."

class Rules:
  ###did not need to put pass as have method below 

  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
  
  ### can also take more arguements than just self 
  
class DistanceConverter:
  kms_in_a_mile = 1.609 ##used class to convert miles to km
  def how_many_kms(self, miles): ##takes self and miles 
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5) ##do not need to use self again in argument as that is always taken as a given first 
print(kms_in_5_miles)
# prints "8.045"

####

class Circle: #class created 
  pi = 3.14  #class variable equals to 3.14
  def area(self, radius): #function created called area with self and radius as arguments 
    return Circle.pi * radius ** 2 ##to return sum of 3.14 (pi) x radius to power of 2

circle = Circle() #variabe set equal to circle class
pizza_area = circle.area(6) ##variable of pizza area equal to function in circle with radius of 6 
teaching_table_area = circle.area(18) ## as above with diff measurement 
round_room_area = circle.area(5730)


####

