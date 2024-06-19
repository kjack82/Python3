# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

## ANy class can be a parent class as syntax is the same. 

class Person:  ## This is a parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() #prints John Doe 

### To create a child class, use the parent class as a paramter when creating child class. 

class Student(Person):
    pass  ## using pass as not adding any other properties or methods 

x = Student("Mike", "Olsen")
x.printname() #Prints Mike Olson

###

# class Student(Person):
#   def __init__(self, fname, lname): ##called automatically every time class being used to create a new object 
#     #add properties etc.
#     ## note as adding to child class, this overrides the init function the parent has.


class Student(Person):
  def __init__(self, fname, lname): 
    Person.__init__(self, fname, lname) # to keep parents init function, need to add it to the block of code 
    
x = Student("Mike", "Olsen")
x.printname()

#### Can also use the super() function 
# this will make the child class inherit all methods and properties from its parent 
# Do not need to use the name of the parent element 
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

### Adding properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear) #prints 2019

## this example 2019 should be variable and passed to Student class when creating new objects, need to add another param to init function

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear) #prints 2019

### Add methods 
# eg Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
