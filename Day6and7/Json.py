## JSOn is a syntax for storing and exchanging data. 
## JSOn is text written with javascript object notation

## Python has built in package called JSON which works with JSON data. 

## USE
import json

# can parse JSOn string to Python using json.loads() method
# Result will be a python dictionary 

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) #prints 30 
print(y) #prints {'name': 'John', 'age': 30, 'city': 'New York'}

## To convert Python to JSON using json.dumps()

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

