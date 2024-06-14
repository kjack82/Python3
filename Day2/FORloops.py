# LOOPS 
#TWO TYPES
#INDEFINITE ITERATION - number of times loop executed depends on how many times condition is met 
#DEFINITE ITERATION - number of times executed decided in advance 

#FOR LOOPS DEFINITE ITERATION - we know how it will loop in advance 

#for keyword inidcates atart of the loop 
# <temporary variable> used to represent the value of the element in the collection the loop is on 
# in keyword separates temp variable from the collection 
# <collection> top loop over, ie a list 
# <action> to do anything on each iteration 

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
  