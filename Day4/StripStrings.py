###REMOVES WHITESPACE
featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'

##CAN ALSO USE TO REMOVE CHARACTER ALTHOUGH WILL THEN NOT REMOVE WHITESPACE 

featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '


####

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = [] ##new empty list

for line in love_maybe_lines:  ##for loop iterating through lines within list
  love_maybe_lines_stripped.append(line.strip())  ## add lines stripped of whitespace to new list 
  
love_maybe_full = '\n'.join(love_maybe_lines_stripped) ##new variable equals new list with lines split to a new line each 

print(love_maybe_full)
## prnts 

# Output-only Terminal
# Output:
# Always
# in the middle of our bloodiest battles
# you lay down your arms
# like flowering mines

# to conquer me home.