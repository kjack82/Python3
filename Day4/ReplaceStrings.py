# The next string method we will cover is .replace(). 
# Replace takes two arguments and replaces all instances of the first argument in a string with the second argument. The syntax is as follows

# string_name.replace(substring_being_replaced, new_substring)

with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)
# 'You_got_the_kind_of_loving_that_can_be_so_smooth'

###

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer") ## to replace Tomer with Toomer 
print(toomer_bio_fixed)

# prints
# Nathan Pinchback Toomer, who adopted the name Jean Toomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Toomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Toomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.

