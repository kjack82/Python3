## Key function is open()
## Takes two aparms, filename and mode. 

## 4 different modes. 
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# can also specify if needs to be ninary or text mode 
# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt")
# The code above is the same as:

f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

## say we have a txt file... caled demofile.txt
#to open - use open() function

f = open("demofile.txt", "r")
print(f.read())

##if located in a different file.. 
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

## read() method allows to only read part of the file 

f = open("demofile.txt", "r")
print(f.read(5)) ##returns first 5 characters of the file 

## readline() method 
f = open("demofile.txt", "r")
print(f.readline()) ##reads one line 
print(f.readline()) ##reads two lines 

## can loop through to read one line at a time
f = open("demofile.txt", "r")
for x in f:
  print(x)

## should always close file once done with it
f = open("demofile.txt", "r")
print(f.readline()) # prints one line then closes file 
f.close()

### WRITING TO EXISTING FILE 
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

###
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
## printsHello! Welcome to demofile2.txt
# This file is for testing purposes.
# Good Luck!Now the file has more content!

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
##prints Woops! I have deleted the content!

### CREATING A NEW FILE 
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "x") ## creates a file called myfile.txt

f = open("myfile.txt", "w") ## creates a new file if it does not exist 

#### DELETING FILES 

##must import the os module and run its os.remove() function

import os
os.remove("demofile.txt")

## can check file exists first 
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

## to delete folder, need to use os.rmdir() method - however can only remove empty folders 
import os
os.rmdir("myfolder")


