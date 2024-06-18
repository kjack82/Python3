# WHILE loops repeatedly execute a code block as long as the condition evaluates to True 
# The condition of  while loop is always checked first before it runs - if the condition is not met, the coe block will never run. 
# Use while loops to run the same task multiple times. For loops used to loop over information once in a list of data. 

# while <conditional statement>:   while is type of loop. Followed by a conditional statement 
#   <action>  ollowed by an action 

## could use a while loop to:
# Check for another line in a file
# Check if a flag has been set
# Check if a user has finished entering values
# Check if something has changed to indicate the code can stop performing. 

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

####
# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')
    
    

