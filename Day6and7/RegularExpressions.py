# Sequence of characters that forms a search pattern
# Can use to check if a string contains a specified search pattern 

# Built in package called re which can be used to work ith regular expressions 

import re ## need to import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) ##using metacharacters - see below 
if x:
  print("YES! We have a match!")
else:
  print("No match")
  ##prints YES! We have a match!
  
  ## findall() function
  # findall	Returns a list containing all matches
  
#   Example
# Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) #prints ['ai', 'ai']

##
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) ## returns empty list if no match found 

### SEARCH FUNCTION search()
# The search() function searches the string for a match, and returns a Match object if there is a match.
# search	Returns a Match object if there is a match anywhere in the string

# If there is more than one match, only the first occurrence of the match will be returned:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

## if no matches, None is returned 

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

### SPLIT split() function
# split	Returns a list where the string has been split at each match

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# can control number of occurrences specifying maxsplit paramter
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

##### SUB FUNCTION sub()
# sub	Replaces one or many matches with a string

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

## can control number of replacements by specifying count param

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#### MATCH OBJECT 
# This is the object returned containing information about search result. If no results - None is displayed
# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

#METACHARACTERS
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group

## SPECIAL SEQUENCES
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

# r"ain\b"	

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

# r"ain\B"	

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

#### SETS
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
	
