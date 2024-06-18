##files also have scope, in the same way as variables in functions and classes etc 

### need to use import to do this 

## Syntax as follows ; 
# from name_of_file import name_of_file 

##example - we have a library file with a function called always_three()

##in script file...

## from library import always_three  -- import function from file 

## always_three()  -- can then call the function 

# Aliasing matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
# plt.plot(x, y)

# # Aliasing calendar as c
# import calendar as c
# print(c.month_name[1])

###

# Three different ways to import modules:
# First way
# import module
# module.function()

# # Second way
# from module import function
# function()

# # Third way
# from module import *
# function()

## can import and use content of another file using import filename 

# file1 content
# def f1_function():
#	  return "Hello World"

# # file2
# import file1

# # Now we can use f1_function, because we imported file1
# f1_function()