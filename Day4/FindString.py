# Another interesting string method is .find(). .find() takes a string as an argument and searching the string it was run on for that string. 
# It then returns the first index value where that string is located.

# Here’s an example:

print('smooth'.find('t'))
# => '4'

print("smooth".find('oo'))
# => '2'  ## it will index the first o

###
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement) ## prints 20 




