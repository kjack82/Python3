#defining a function

#def function_name():  always put def then the function name then () and :
    #tasks go here     must indent function tasks 

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
  
trip_welcome() #to call function 
  
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
  
directions_to_timesSq()  #to call function 

#####

def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")

trip_welcome()

#will print
# Woah, look at the weather outside! Don't walk, take the train!
# Welcome to Tripcademy!
# Let's get you to your destination.


print("Checking the weather for you!")

def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()

## If unindent the false alarm print statement, this will be printed before the looks great line 

### PARAMETERS

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

trip_welcome("Times Square") # prints above two lines with Times Square as destination

### RETURN 

# A return keyword is used to return a value from a Python function. 
# The value returned from a function can be assigned to a variable which can then be used in the program.

def check_leap_year(year): 
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."

year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value) # 2018 is not a leap year.


#### SCOPE

#If a variable is declared outside of function, it can be used again anywhere. 
#If a variable is defined within a function, it cannot be used outside of it. 


favorite_locations = "Paris, Norway, Iceland" ## as defined outside, can be used in btoh functions 

def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()
 ####

## Can return multiple values too

def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
  # Return all three values:
  return x_squared, y_squared, z_squared

three_squared, four_squared, five_squared = square_point(3, 4, 5)
