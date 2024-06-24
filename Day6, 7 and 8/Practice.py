age = 20
print(age)
age = 30
print(age)

name = input("What is your name? ")  ##asks in terminal for name, I enter Kate 
print("Hello " + name) ## once anssered, termnal then prints Hello Kate 

birth_year = input("What is your birth year? ")
age = 2024 - int(birth_year) ## converts a string to an integer
print(age)

## Have the following 

int()  ## converts to an integer
str() ## converts to a string
float() ## converts to a float 
bool() ## converts to a boolean 


first = input("First: ")
second = input("Second: ")
sum = int(first) + int(second)
print(sum)

first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

## can also do as follows 
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))

course = "Python for beginners"    ## this is an object

## An object is like an object in the real world

#Have lots of built in methods 

course.upper()  ## puts to capitals
course.lower() ## puts to lower case 
course.find("y") ## will find the first instance of "y" which will be 1 as index sytartes at 0 is case sensitive too 
course.replace("for", "4")
print("Python" in course)

## division. If use / then will get a float, if use // will get an integer

x = 3 > 2  ## will give a boolean value of true as 3 greater than 2 
x = 3 < 2 ## will give false 

price = 5
print(price > 10 and price < 30) ## gives false 
print(price > 10 or price < 30) ## gives true as 5 is less than 30 

#####
    
weight = float(input("Weight: "))
measure = input("(K)gs or (L)bs? ")

if measure.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


i = 1

while i <= 5:
    print(i)
    i = i + 1  ## prints 1, 2, 3, 4, 5
    

i = 1

while i <= 10:
    print(i * '*')
    i = i + 1  ## prints *, **, ***, ****, ***** and so on until 10 *
    
###

numbers = [1, 2, 3, 4, 5, 6]
numbers.clear() ## will remove all numbers 

numbers.insert(0, -1)
print(numbers)
numbers.remove(5)
print(numbers)

print(1 in numbers) ## will return True 

print(len(numbers))


numbers = [1, 2, 3, 4, 5]
for item in numbers:  ##for loop will only iterate over each item(number) once then move to the next one after printing it.
    print(item)
    
    
## can use while loop to achieve the same thing, but more code required. 

i = 0
while i < len(numbers):  #states that while i is less than the length of numbers list
    print(numbers[i])  ##print the i(index) of numbers
    i = i + 1 ## and add 1 to i
    
    ### can use a for loop with any object where there is a sequence 
    
numbers = range(5)
for number in numbers:
    print(number)
    ## prints 0 -4 as index starts at 0 

numbers = range(5, 10)
for number in numbers:
    print(number) ##v prints 5- 9 
    
numbers = range(5, 25, 5) #last digit counts up in 5
for number in numbers:
    print(number)  ## will print 5, 10, 15, 20