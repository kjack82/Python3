### PARAMETERS

def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")

trip_welcome("Times Square") # prints above two lines with Times Square as destination

# paramter is destination (the word)
# arguement is Times Square as this is giving a value to the paramter. 

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")  
#prints Looks like you are planning a trip to visit Grand Central Station
# You can use the public subway system to get to Grand Central Station

### MULTIPLE PARAMS AND ARGUEMENTS - USE OF COMMAS 

def trip_welcome(origin, destination):
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)
  
trip_welcome("Prospect Park", "Atlantic Terminal")

# prints Welcome to Tripcademy
# Looks like you are traveling from Prospect Park
# And you are heading to Atlantic Terminal

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  return trip_total

print(calculate_expenses(200, 100, 100, 5))


### 3 DIFFERENT TYPES OF ARGUEMENTS ###

# Positional arguments: arguments that can be called by their position in the function definition. BASED ON THEIR POSITION WITHIN THE BRACKETS. 

# Keyword arguments: arguments that can be called by their name. WHERE USE KEYWORDS AND NOT FOLLOW ORDER

# Default arguments: arguments that are given default values. USE = WITHIN THE FUNCTION PARMS ITSELF 
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
  
  # Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)



def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")  #prints in order 

trip_planner("Denmark", "France", "Germany")  #prints in order 

trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India") #not in order, put in order of keywords, ie Iceland, India then Germany

trip_planner("Brooklyn", "Queens") # prints Brooklyn, Queens, Codecademy HQ as not overridden 

help("string")

### USING BUILT IN FUNCTIONS

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)  # PRINTS 15.50 AS THIS IS HIGHEST 

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price) #PRINTS 2.00 AS THE LOWEST 

rounded_price = round(tshirt_price, 1)  # need to add first arguement as what is to be rounded, second arguement is to how many decimnal places 
print(rounded_price) #PRINTS 9.80 ROUNDED TO 1 DECIMAL PLACE 





