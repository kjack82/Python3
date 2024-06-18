# These are arrays 

# Start with [ and ends with ].
# Separated by a comma and a space
# start with 0. and run for the length of the list - 1
# to access an index of a list, need to use [], so could be [0], [1] or even [i] if referring to looping through the list 

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

#can mix data types

ints_and_strings = [1, 2, 3, "four", "five", "six"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]
 #Empty list 
empty_list = []

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)  #adds 5 to the end 
print(example_list)

#Using Remove
example_list.remove(5)  #removes 5 from the end 
print(example_list)

orders = ["daisies", "periwinkle"]
print(orders) #prints above 

orders.append("tulips")
orders.append("roses")

print(orders) # adds additional two items 

#adding lists together
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
# Prints ['cake', 'cookie', 'bread', 'biscuit', 'tart']

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders

print(orders_combined)