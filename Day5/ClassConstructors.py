## dunder methods as double underscore
## first dunded method is __init__()
## used to initise a newly created object and is called every time class is instantised

## Methods used to prepare an object being instantised are called constructors
## In Python - normally referring to __init__() method 

class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter() ##creating an instance of shouter class
# prints "HELLO?!"

shout2 = Shouter() ## creating another instance of shouter class
# prints "HELLO?!"

## Notice Shouter( ) is like calin a function, can also pass arguements

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

