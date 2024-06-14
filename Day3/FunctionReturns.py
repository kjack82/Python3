def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate  #when called, it will return the value or calc 

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")
#prints 100 dollars in US currency would give you 140 New Zealand dollars

current_budget = 3500.75
shirt_expense = 9 

def print_remaining_budget(budget): ##first function
  print("Your remaining budget is: $" + str(budget)) ##prints string confrming currentl budget variable 

print_remaining_budget(current_budget) ## prints 3500.75

# Write your code below: 
def  deduct_expense(budget, expense):  ## secon function
  return budget - expense  ##when called, will return the sum of budget less expense

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)  #new variable, equal to called function

print_remaining_budget(new_budget_after_shirt) #printing variable, which has function within it.   ##PRINTS 3491.75

#######

weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']  #LIST OF WEATHER DATA DEFINED 

def threeday_weather_report(weather): #FUNCTION DEFINIED 
  first_day = " Tomorrow the weather will be " + weather[0]  #VARIABLE DEFINED CALLS INDEX FROM LIST 
  second_day = " The following day it will be " + weather[1]#VARIABLE DEFINED
  third_day = " Two days from now it will be " + weather[2]#VARIABLE DEFINED
  return first_day, second_day, third_day #RETURNS THREE DAYS OF VARIABLES 

monday, tuesday, wednesday = threeday_weather_report(weather_data) ## VARIABLE DECLARED WHICH IS EQUAL TO CALL OF THE FUNCTION

print(monday)
print(tuesday)
print(wednesday)

##PRINTS 
# Tomorrow the weather will be Sunny
# The following day it will be Sunny
# Two days from now it will be Cloudy

###

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

#prints Rome, Venice, Florence

###

def trip_planner_welcome(name):  ##defined function
  print("Welcome to triplanner v1.0 " + name) ##which prints an niitial statement with name passed as arguement 

trip_planner_welcome("Kate")

def estimated_time_rounded(estimated_time):  ##defined new function that will round estimated time 
  rounded_time = round(estimated_time) #variable set as rounded time, equal to round of estimated time 
  return rounded_time #to return variable (rounded time)

estimate = estimated_time_rounded(20.4)  #new variable, estimate, equal to function above with arguuement of 20.4

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):  ##new function defined
  print("Your trip starts off in " + origin) #print statements 
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) +  " hours") ##this one needs str() a the arguement is an integer 

destination_setup("Perth", "Manchester", estimate, "Plane")  ##calling function above which will round 20.4 to 20 and overwrite car to plane. If left last one blank then car would be printed. 

# Prints Welcome to triplanner v1.0 Kate
# Your trip starts off in Perth
# And you are traveling to Manchester
# You will be traveling by Plane
# It will take approximately 20 hours