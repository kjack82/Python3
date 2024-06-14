class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"


## hasattr() will return true is an object has a given attribute
## getattr() is a function that will return the value of a given object and attribute 

# The syntax and parameters for these functions look like this:

# hasattr(object, “attribute”) has two parameters:

# object : the object we are testing to see if it has a certain attribute
# attribute : name of attribute we want to see if it exists

# getattr(object, “attribute”, default) has three parameters (one of which is optional):

# object : the object whose attribute we want to evaluate
# attribute : name of attribute we want to evaluate
# default : the value that is returned if the attribute does not exist (note: this parameter is optional)

# Calling those functions looks like this:

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

##checking to see ig the attributeless object has fake_attribute attribute (using has)
##Then it tries to retrieve the attribute using (get)

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]  ## different data types 

for element in can_we_count_it: #for loop iterating through can we count it 
  if hasattr(element, "count"): #if any of the items hve count
    print(str(type(element)) + " has the count attribute!") ##print statement 
  else: ##else 
    print(str(type(element)) + " does not have the count attribute :(") ##print this 
    
    ####### SELF 
    
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"
 
 
 #########
 
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())