# RANGE FUNCTION

# range will have numbers from 0, upto the number you inout, -1. 

my_range = range(10)
print(my_range)  #will output range(0, 10)

#Have to use list function to get the range to list the numbers individually. 
print(list(my_range)) 
#will output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number_list = range(9)
print(list(number_list)) # numbers through to 8

zero_to_seven = range(8)
print(list(zero_to_seven)) #numbers through to 7 

my_list = range(2, 9) #starting number in range is 2, last number is 9 -1
print(list(my_list)) #outputs [2, 3, 4, 5, 6, 7, 8]

# Can skip numbers too. 
my_range2 = range(2, 9, 2) #means start at 2, upto 9-1, but go up in 2s 
print(list(my_range2)) #output [2, 4, 6, 8]

my_range3 = range(1, 100, 10)
print(list(my_range3))  #outputs [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

range_five_three = range(5, 15, 3)
print(list(range_five_three)) #outputs 5, 8, 11, 14]

range_diff_five = range(0,40, 5)
print(list(range_diff_five)) #outputs [0, 5, 10, 15, 20, 25, 30, 35]

# LENGTH   (LEN() WILL GIVE THE LENGTH OF A LIST

my_list = [1, 2, 3, 4, 5]

print(len(my_list)) #outputs 5 


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100) #starts at 2, up to 2999, in 100's 

long_list_len = len(long_list)
print(long_list_len) #outputs 18 

big_range_length = len(big_range)
print(big_range_length) #outputs 30


# SORTED BUILT IN FUNCTION 

#THIS DIFFERS FROM A .SORT. IT BECOMES BEFORE A LIST INSTEAD OF AFTER. AND GENERATES A NEW LKST RATHER THAN MODIFYING ORIGINAL LIST 

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

#can create a new list called sorted names 
sorted_names = sorted(names)
print(sorted_names)  #prints ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

#names will still be in the same order as before 


games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games_sorted)  #prints ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']
print(games) #prints ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
