## Modules are referred to as libraries or packages
## A directory that holds a collection of modules

##syntax as follows: from module_name import object_name

from datetime import datetime ## just module that can be used..

current_time = datetime.now()
print(current_time)

### RANDOM is one too

import random

random.choice() ## which takes a list as an argument and returns a number from the list
random.randint() ## which takes two numbers as arguments and generates a random number between the two numbers you passed in


import random

# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)] 
#This is a list comprehension that repeats the random.randint(1, 100) call 101 times (since range(101) generates numbers from 0 to 100, inclusive, resulting in 101 iterations).


# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

##### NAMESPACES 
# Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

# Fortunately, this name can be altered by aliasing using the as keyword:

# import module_name as name_you_pick_for_the_module



#random.sample takes a list and randomly selects k items from it
# new_list = random.sample(list, k)

nums = [1, 2, 3, 4, 5]
sample_nums = random.sample(nums, 3)
print(sample_nums) # 2, 5, 1

#####

# import codecademylib3_seaborn  ## this is a codecademy module 
# from matplotlib import pyplot as plt  ## this imports pyplot from matplotlib and renames plt for convenience, popular for creating static, animated and interacive visualisations in python
# import random ##imports random which provdes functions for generating random numbers 

# Add your code below:
#   numbers_a = range(1, 13) ##variable equal to a range of numners from 1 - 13 
#   numbers_b = random.sample(range(1000), 12) ##creates a list called b that will create 12 unique random numers from 0 - 999
#   plt.plot(numbers_a, numbers_b) ##plots a line plot with generated numbers 
#   plt.show()  ##displays the line plot. New plot each time command runs 

###




