# LOOPS 
#TWO TYPES
#INDEFINITE ITERATION - number of times loop executed depends on how many times condition is met 
#DEFINITE ITERATION - number of times executed decided in advance 
# Infinite loops, meaning code normally wrong as will keep going - press contrl + c tp stop this if it happens 

#FOR LOOPS DEFINITE ITERATION - we know how it will loop in advance. It will loop over every item and perform an action.
# INvolves assigning a temp variable. 
# Need to indent the actions. 

# Use while loops to run the same task multiple times. For loops used to loop over information once in a list of data. 

#for keyword inidcates start of the loop 
# <temporary variable> used to represent the value of the element in the collection the loop is on 
# in keyword separates temp variable from the collection 
# <collection> top loop over, ie a list 
# <action> to do anything on each iteration 
# can use break keyword to exit the loop immediately. 
# can use continue keyword inside a loop to skip the remaining code inside that loop, and move to the next iteration. 

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for ingredient in ingredients:  #ingredient is temp variable , ingredients is the collection 
  print(ingredient)  #print ingredient is the action 
  
  #temp variable does not need to be defined before and can be anything. 
  
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for game in sport_games:
  print(game)
  
## USING BREAK 

numbers = [0, 254, 2, -1, 3]

for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break
  print(num)
  
# 0
# 254
# 2
# Negative number detected!

####

# using continue 

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# Print only positive numbers:
for i in big_number_list:
  if i < 0:
    continue
  print(i)
  
  ### 
  
# USING RANGE AND FOR LOOPS

six_steps = range(6)  #sets up a range of 0-6
for temp in range(6): #temp is temp variable 
  print("Learning Loops!")  #this is printed 6 times 
  
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))  #using this to see how many steps it takes to run the loop. +1 as start at 0 
  
#prints
# Loop is on iteration number 1
# Loop is on iteration number 2
# Loop is on iteration number 3
# Loop is on iteration number 4
# Loop is on iteration number 5
# Loop is on iteration number 6

promise = "I will finish the python loops module!"

for promise in range(5):
  print("I will finish the python loops module!")


####

from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")