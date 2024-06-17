class Employee():
  def __init__(self, name):
    self.name = name

argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

##this prints out information about file name, where it is stored in the memory etc 

######

## __rep(__() 
# This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter,
# self, and must return a string.

class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

###

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza) ##prints Circle with radius 6.0
print(teaching_table) ## "" "" 18.0
print(round_room)## "" "" 5730.0


