#Can only be true or false, cannot be subject to opinion

# Dogs are mammals is a boolean expression
# Dogs make the best pets is not, as down to opion and others may feel other animals make best pets 

#Equals: ==
#Not equals: !=

1 == 1     # True

2 != 4     # True

3 == 5     # False

'7' == 7   # False

#Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:

#Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:

set_to_true = True
set_to_false = False

#You can also set a variable equal to a boolean expression.

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

#These variables now contain boolean values, so when you reference them they will only return the True or False values of the expression they were assigned.

print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True

print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True

my_baby_bool = "true"
print(type(my_baby_bool)) #will show as a string 

my_baby_bool_two = True
print(type(my_baby_bool_two))  #will show a a bool

#use type rather than typeOf which is used in javascript

