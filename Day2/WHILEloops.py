# WHILE OOPS ARE INDEFINITE 

# while <conditional statement>:   while is type of loop. Followed by a conditional statement 
#   <action>  ollowed by an action 

count = 0  #count initially 0 
while count <= 3: #cpnditional state - while count is less than or equal to 3
  # Loop Body
  print(count)  #count is printed 
  count += 1  #incremented by 1 
  
  #this continues to loop until the count is 4 then is stops 
  
  
  # While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")



countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")  #final print must not be indented 
#prints 10 down to 0, then we have liftoff printed 


#WHILE LOOPS WITH LENGTH 
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

length = len(ingredients)  #length will be 5 
index = 0  #index starts at 0 

while index < length: #start of while loop. We compare index variable to length of stored list, first loop will be 0 < 5 
  print(ingredients[index])  #prints part of list 
  index += 1 #keep iterating through the list until gets to 5 


python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1
  
# prints I am learning about variables
# I am learning about control flow
# I am learning about loops
# I am learning about modules
# I am learning about classes

