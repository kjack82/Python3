##string method syntax always as follows

##   string_name.string_method(arguments)

# There are three string methods that can change the casing of a string. These are .lower(), .upper(), and .title().

# .lower() returns the string with all lowercase characters.
# .upper() returns the string with all uppercase characters.
# .title() returns the string in title case, which means the first letter of each word is capitalized.

favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)
# => 'smooth'

####however create a new string, the old string not changed. 

poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()

print(poem_title)  #spring storm
print(poem_title_fixed) #Spring Storm

poem_author_fixed = poem_author.upper()
print(poem_author) #William Carlos Williams 
print(poem_author_fixed) #WILLIAM CARLOS WILLIAMS 

###########
### SPLITTING STRINGS 
## SYNTAX string_name.split(delimiter)

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words) ##prints ["The", "sky", "has", "given", "over"]

####
###splitting with a letter 

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
# => ['sa', 'ta', 'a'] ##removes n and breaks up the word 
print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', ''] ##removes a but gives empty "" as split on the end letter 

#####

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")  ##split from comma
print(author_names) ##print variable with the names split 

###

author_last_names = [] ##new variable with emplty list
for name in author_names:  ##for loop to iterate through list of names 
  author_last_names.append(name.split()[-1]) ## add author last name to nw list splitting by spaces 
  
print(author_last_names)

# We can also split strings using escape sequences. Escape sequences are used to indicate that we want to split by something in a string that is not necessarily a character. The two escape sequences we will cover here are

# \n Newline
# \t Horizontal Tab
# Newline or \n will allow us to split a multi-line string by line breaks and \t will allow us to split a string by tabs. \t is particularly useful when dealing with certain datasets because it is not uncommon for data points to be separated by tabs.

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines) ##prints each line to it's own list 







