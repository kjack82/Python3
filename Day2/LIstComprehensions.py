numbers = [2, -1, 79, 33, -45]  #list
doubled = [] #new variable with empty list 

for number in numbers:  #for loop, temp variable is number looping thrpough numbers list
  doubled.append(number * 2)  #doubled then adds number x 2 to the list 

print(doubled)
#outputs [4, -2, 158, 66, -90]

#can also do it this way 
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers] #num is temp variable
print(doubled)


grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]
print(scaled_grades)
#prints [100, 98, 72, 86, 84, 99, 58, 67]


numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled) #would print [-2, -90]

#USING COMPREHENSIVE
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled) #PRINTS THE SAME AS ABOVE 

#CAN USE IF AND ELSE 
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled) #PRINTS [6, -2, 237, 99, -90]



numbers = [2, -1, 79, 33, -45]

no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height >161] #height is temp variable, in a for looop to iterate through height in list of heights  if heights above 161 
print(can_ride_coaster) #prints new variable with only those heights above 161


single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for digit in single_digits:
  print(digit)
  squares.append(digit * digit) #adding calc of d x d to new squares list
  print(squares)

  cubes = [digit ** 3 for digit in single_digits] #comprehensive digit to power of 3 for digits in signle digits list 
  print(cubes)