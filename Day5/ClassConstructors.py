## dunder methods as double underscore
## first dunded method is __init__()
## used to initise a newly created object and is called every time class is instantised

## Methods used to prepare an object being instantised are called constructors
## In Python - normally referring to __init__() method 

class Shouter:
  def __init__(self): ##instance method that initialises a newly created object - ensures it is in a known, valid state before it is used and prepares for operations
    print("HELLO?!")

shout1 = Shouter() ##creating an instance of shouter class
# prints "HELLO?!"

shout2 = Shouter() ## creating another instance of shouter class
# prints "HELLO?!"

## Notice Shouter( ) is like calling a function, can also pass arguements

## new example just using default construtor
class GeekforGeeks:
 
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"
 
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
 
 
# creating object of the class
obj = GeekforGeeks()
 
# calling the instance method using the object obj
obj.print_Geek()  #prints GeeksforGeeks

###

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

######

class Circle: #class defined
    pi = 3.14
    
    def __init__(self, diameter): ##initialiser method, init the constructor called as class created
        self.diameter = diameter
        print(f"New circle with diameter: {self.diameter}") ## f used to format the expression so the whole thing can be output as a string similar to str.xxx

# Create a circle teaching_table with diameter 36
teaching_table = Circle(36) ##cteates an instance of circle class
print(teaching_table)


####
class Addition:
    first = 0
    second = 0
    answer = 0
 
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
 
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
 
    def calculate(self):
        self.answer = self.first + self.second
 
 
# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)
 
# creating second object of same class
obj2 = Addition(10, 20)
 
# perform Addition on obj1
obj1.calculate()
 
# perform Addition on obj2
obj2.calculate()
 
# display result of obj1
obj1.display()
 
# display result of obj2
obj2.display()

##output
# First number = 1000
# Second number = 2000
# Addition of two numbers = 3000
# First number = 10
# Second number = 20
# Addition of two numbers = 30