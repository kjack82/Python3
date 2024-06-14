# List Methods

# .count()  - counts number of occurences of an element in a list 
# .insert()  - inserts an element into a specific index of a list 
# .pop()  - removes an element from a specific index of a list 
# range()  - Python function to create a sequence of integers
# len()  - Python function to get the length of a list 
# .sort() / sorted()  - sorts a list, both a method and built in function 

# Example syntax for methods
# list.method(input)

# Example syntax for a built-in function 
# builtinfunction(input)

# INSERT

store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")
print(store_line) 
 # will print ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']

 #expects two inputs - numerical index first, followed by the value of the new input second. 
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# REMOVE ---- POP

# The .pop() method takes an optional single input:

# The index for the element you want to remove.

cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"] # NEW LIST
removed_element = cs_topics.pop()  #SET A NEW VARIABLE WHICH WILL show the item that is removed 
print(cs_topics) #prints list with Clowns 101 removed
print(removed_element) # prints Clowns 101 as the item that 

#can also add an index within the () and this will remove a specific item 

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()  #removes python3 from end
print(data_science_topics)

data_science_topics.pop(3)  #removes Algorithms 
print(data_science_topics)


#SLICING LISTS Can slice or divide a lst 
letters = ["a", "b", "c", "d", "e", "f", "g"]

sliced_list = letters[1:6]  #means start at index 1, end at index 6 although 6 will not be included 
print(sliced_list)  #outputs ["b", "c", "d", "e", "f"]


suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2] #to include 1st and second items only 

print(beginning) #prints shirt and shirt 

middle = suitcase[2:4]  # inludes 3rd and 4th only 
print(middle)  #prints pants and pants



fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
print(fruits[:3]) # will slice from 0 upto index 3 (not including 3)  - outputs apple, cherry and pineapple

print(fruits[-2:])  #will slice the last 2 elements, outputting orange, mango
print(fruits[:-1])  #slice all but the last emenent, prints apple, cherry, pineapple, orange 


suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

last_two_elements = suitcase[-2:]   #to slice and show only last 2 of the list
print(last_two_elements) #prints pajamas, books

slice_off_last_three = suitcase[:-3]  #to show everything other than the last 3 items 
print(slice_off_last_three)  #prints shirt, shirt, pants


#COUNT METHOD 
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")  #to count how many times i appears 
print(num_i)  #outputs 4 


#can count in 2d lists too. 

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])  #to check how often 100, 200 appears 
print(num_pairs) #prints 2 


votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes)   #prints 9 as Jake shows 9 times 

#SORT METHOD NOTE CANNOT STORE WITHIN A VARIABLE IT WILL SHOW AS NONE. USE TO MODIFY THE LIST DIRECTLY 

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()  #will sort in alphbetical order 
print(names)  #outputs ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
names.sort(reverse=True) #will go in reverse order 
print(names) #prints ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']

addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses) #PRINTS ['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave', '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace']


names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort() #if print it outs ['Albus', 'Harry', 'Hermione', 'Ron', 'Sirius']


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities) #prints ['Rome', 'Paris', 'New York', 'Los Angeles', 'London']


