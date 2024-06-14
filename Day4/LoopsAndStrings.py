#### STIRNGS ARE LISTS 

def print_each_letter(word):  ## FUNCTION DEFINED 
  for letter in word:  ## for each letter in word
    print(letter) ##print letter 

favorite_color = "blue" ##variable defined 
print_each_letter(favorite_color) ##calling the function to proint each letter 
# => 'b'
# => 'l'
# => 'u'
# => 'e'


def get_length(word): ##function defined 
  count = 0 ##count set to 0 
  for letter in word: ##for loop, iterating through letters in the word
    count += 1  ##count increases by 1 
  return count ##return count 

word_len = get_length("Tessa") ##new variable set to calling of function with word of Tessa
print(word_len) ##prints 5 


#####
favorite_fruit = "blueberry"  ## variable of blueberry 
counter = 0 ##counter set to 0 
for character in favorite_fruit: ##for loop iterating through characters in fruit
  if character == "b": ## if charcter equal to be 
    counter = counter + 1  ## counter is equal to counter + 1 
print(counter)  #prints character 

#####

def letter_check(word, letter):
  for char in word:
    if char == letter:
      return True
   
  return False
  
  print(letter_check("strawberry", "a"))
  
  ### can use word in 
  print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

##can use full words 
print("blue" in "blueberry")
# => True
print("blue" in "strawberry")
# => False

##can use in, and and and no 

print("e" in "blueberry" and "e" in "carrot")
# => False
print("e" in "blueberry" and not "e" in "carrot")
# => True


####

def contains(big_string, little_string):
  if little_string in big_string:
    return True

  return False

contains("Blue skies", "blue")
print(contains)

####

def common_letters(string_one, string_two): ##function defined
  list_letters = []  ##empty list created 
  for char in string_one: ##for loop to iterate through characters in string 1
    if (char in string_two) and not (char in list_letters): ##if characters in string 2 and not in new list
      list_letters.append(char) ## append the letter to the new list
  return list_letters ##return to new list  ####MUST RETURN OUTSOIDE OF THE LOOP SO TAKE INDENTATIO BACK

checker = common_letters("Monkey", "Money") 
print(checker) ##prints m, o, n, e, y

