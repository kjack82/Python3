# Built-in Functions

# .format()
# Used to format different types of objects into strings.

# abs()
# Returns the absolute value of a numeric argument.

# all()
# Returns True if every item in an iterable evaluates to True, otherwise, it returns False.

# any()
# Takes in an iterable object such as a list or tuple and returns True if any of the elements in the iterable are True. If none of the elements in the iterable are True, returns False.

# ascii()
# Receives as input an object containing string data, and returns the object as a printable representation with escapes for non-ASCII characters (accented characters).

# bin()
# Converts an integer into its binary equivalent string.

# bool()
# Converts a value to a Boolean True or False value.

# breakpoint()
# Engages, configures, and changes the debugger program used in a script.

# bytearray()
# Returns an array of the given bytes of an object.

# bytes()
# Returns a byte immutable object representing the given bytes of an object.

# callable()
# Returns True if an object is callable, and False if an object is not callable.

# chr()
# Returns Unicode characters represented by integers ranging between 0 and 1,114,111.

# classmethod()
# Converts a given function into a class method.

# compile()
# Returns a runnable code object created from a string.

# complex()
# Converts a given string into a complex number.

# delattr()
# Allows the user to delete attributes from an object.

# dict()
# Initializes a new dictionary from mapping n-number of object (key, value) pairs.

# dir()
# Returns the list of valid attributes of the passed object.

# divmod()
# Returns the quotient and remainder of the division of two numbers.

# enumerate()
# Returns a list of tuples containing an index and an element for each of the elements in an iterator.

# eval()
# Returns the value of a Python expression passed as a string.

# exec()
# Executes a code object or string containing Python code.

# filter()
# Returns a filter object that applies a function to each item in an iterable and returns the values that are True.

# float()
# Returns a float value based on a string, numeric data type, or no value at all.

# frozenset()
# Returns a new frozenset using an optional iterable object such as a string or list.

# getattr()
# Returns the value of the named property in the specified object.

# globals()
# Returns a dictionary with all the global variables and symbols for the current program.

# hasattr()
# Returns True if an object has an attribute and False otherwise.

# hash()
# Returns the hash value as a fixed sized integer.

# help()
# Displays documentation of an object using the Python help utility.

# hex()
# Converts an integer number to a lowercase hexadecimal string.

# id()
# Gives a unique number for any object in Python.

# input()
# Prompts the user for data and returns it as a string.

# int()
# Takes in a value that can be converted into an integer, and returns a copy of the value in the int datatype.

# isinstance()
# Returns True if the given object is the specified type. Otherwise the function will return False.

# issubclass()
# Returns True if a given class is a subclass of one or more classes.

# len()
# Returns the length of an object, which can either be a sequence or collection.

# list()
# Returns a list from an iterable.

# map()
# Returns an iterator that takes a function and applies it to every item in an iterable.

# max()
# Returns the highest value from values given or an iterable.

# memoryview()
# Creates a memoryview object that allows Python code to access the internal data of an object without making a copy of it.

# min()
# Returns the lowest value from values given or an iterable.

# next()
# Returns the next element from an iterable object.

# oct()
# Used to get an octal value of an integer number

# open()
# Used for opening files in a Python program.

# ord()
# Returns the integer that represents the Unicode character argument.

# pow()
# Returns the value of a base number x to the power of an exponent y, with an optional modulus z.

# print()
# Prints the string representation of an object.

# property()
# Declares a range of functions to manipulate class attributes.

# range()
# Returns a sequence of numbers based on the given range

# repr()
# Returns a printable string describing the object that is passed in.

# reversed()
# Takes in an iterable object, such as a list, string, or a tuple and returns a reversed iterator object.

# round()
# Takes a number and an integer as parameters, and returns the number with decimal places equal to the integer.

# set()
# Returns a new set based on an optional iterable object such as a list.

# setattr()
# Sets the value of the attribute of an object.

# sorted()
# Takes in an iterator object, such as a list, tuple, dictionary, set, or string, and sorts it according to a parameter.

# staticmethod()
# Transforms a method to a static method.

# str()
# Takes in a value that can be converted into a string, and returns a copy of the value in the string datatype.

# sum()
# Takes in an iterable object, such as a list or tuple, and returns the sum of all elements.

# super()
# Returns a temporary object that allows a given class to inherit the methods and properties of a parent or sibling class.

# tuple()
# Creates a new tuple.

# type()
# Returns the data type of the argument passed to the function.

# vars()
# Returns the __dict__ attribute of an object.

# zip()
# Takes multiple iterators as input and returns a single zip object made up of a list of tuples.

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

rounded_price = round(tshirt_price, 1)  # need to add first arguement as what is to be rounded, second arguement is to how many decimnal places 
print(rounded_price)