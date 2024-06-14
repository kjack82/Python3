def divisible_by_ten(nums): ## set a function with a param of nums
  count = 0  ##set a variable count
  for number in nums:  #set a for loop to iterate trhough the numbers in nums
    if (number % 10 == 0): ## if number can be divided by 10
      count += 1 ## add 1 to the count 
  return count  ## return the total count 


print(divisible_by_ten([20, 25, 30, 35, 40]))  ##prints 3

####

def add_greetings(names):  ##defined function for add gretings - names is param 
  new_list = []  ## set an empty list 
  for name in names:  ##for loop to iterate through name in names 
    new_list.append("Hello, " + name) ## new list to append (add) Hello + name 
  return new_list  ## return new list 

print(add_greetings(["Owen", "Max", "Sophie"]))  ##prints ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']


####

def delete_starting_evens(my_list):  ##define new function
  while (len(my_list) > 0 and my_list[0] % 2 == 0):  ##while loop, if length of list greater than 0 and number in list is even
    my_list = my_list[1:]  ## remove number from list
  return my_list ## return updated list 

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))  ##prints [11, 12, 15]
print(delete_starting_evens([4, 8, 10])) ##print []

####

def odd_indices(my_list): ##define function
  new_list = [] ##creates empty list 
  for index in range(1, len(my_list), 2):  ## for inex in range from 1, through length of list, then every 2 steps 
    new_list.append(my_list[index]) ##append new list with result 
  return new_list ##return new list 

print(odd_indices([4, 3, 7, 10, 11, -2]))  ##prints 3, 10, -2

####

def exponents(bases, powers): ##new function defined 
  new_list = []  ##empty list
  for base in bases: ##for loop through first list
    for power in powers: ##second for loop thrpugh second list 
      new_list.append(base ** power) ## new list to add sum of number from first list ** number from second list (to power of)
  return new_list  ##return new list 


print(exponents([2, 3, 4], [1, 2, 3]))  ##prints [2, 4, 8, 3, 9, 27, 4, 16, 64]