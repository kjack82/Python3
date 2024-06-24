## PROCESS OF EXTRACTING DATA FROM WEBSITES

# STEP 1

#require requests module. Needed to make rHTTP requests to a specific URL 
#Python provides built in functality. 

### python3 -m pip install requests 

## Can use GET, POST, PT, PATCH or HEAD rquests 

# Example of using GET request 

import requests

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)  ###gives a very long long long box of code 

#### USING BEAUTIFUL SOUP LIBRARY 

# Helps to study a document and remove what is not needed . Makes a document prettier and easier to read 

## INSTALL by typing python3 -m pip install beautifulsoup4

