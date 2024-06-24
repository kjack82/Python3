# SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
# TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
# NameError: This exception is raised when a variable or function name is not found in the current scope.
# IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
# KeyError: This exception is raised when a key is not found in a dictionary.
# ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
# AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
# IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
# ImportError: This exception is raised when an import statement fails to find or load a module.

# try and except.Can use this to handle errors. 

# The TRY block lets you test a block of code for errors.

# The EXCEPT block lets you handle the error.

# The ELSE block lets you execute code when there is no error.

# The FINALLY block lets you execute code, regardless of the result of the try- and except blocks.

# try:
#   print(x)
# except:
#   print("An exception occurred") ##prints an exception occurred
  
# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:
  
## can raise more than one exception block s well. 

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined") ##prints this 
# except:
#   print("Something else went wrong")
  
  ## Can use else within the block too. 
  
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") ##prints hello, nothing went wrong as as the block ran without error. 
  
## Finally can be used and will be executed regardless of whether there's an error or not 
# try:
#   print(x)
# except:
#   print("Something went wrong") ##prints this 
# finally:
#   print("The 'try except' is finished") ##then this 

## another example 

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
  #prints something went wrong when writing to the file
  
  
  ## Can throw an exception using the raise keyword
  x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") #prints Traceback (most recent call last):File "demo_ref_keyword_raise.py", line 4, in <module> raise Exception("Sorry, no numbers below zero")
# Exception: Sorry, no numbers below zero

####

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
# prints 
# Traceback (most recent call last):
#   File "demo_ref_keyword_raise.py", line 4, in <module>
#     raise Exception("Sorry, no numbers below zero")
# Exception: Sorry, no numbers below zero

  
  
  