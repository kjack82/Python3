favorite_fruit = "blueberry"
print(favorite_fruit[1])

##prints l as sequenced from 0 like lists 

###can slice a string too. First number is the start letter, end number means will finish by then, so will not include that letter. 
my_name = "Kate Prothero"
print(my_name[1:5])

first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
##prints Villa - this method with number behind the : means it will start at the beginning and end at the number after :

#can do the opposite way round so 3: would mean start at 3rd indice and run to te end 

### CONCATENATING STRINGS 

fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix

print(favorite_fruit)  ##prints blueberries

#####

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):  ##function defined
  return first_name[:3] + last_name[:3] ##which returns first 3 letters from both names 

new_account = account_generator(first_name, last_name)  ##variable equal to the call of this function 
print(new_account) ##prints JulBle

favorite_fruit = "blueberry"

length = len(favorite_fruit)

print(length)
# Output: 9

fruit_sentence = "I love blueberries"

print(len(fruit_sentence))  ###NOTE SPACES COUNTED TOO 
# Output: 18

last_char = favorite_fruit[len(favorite_fruit)-1]  ##THIS WILL GET LAST CHARACTER, NEED TO USE -1 AS INDEX STARTS AT 0 

print(last_char)
# Output: y

## CAN SLICE THE LAST SEVERAL CHARACTRS TOO USING LEN 
length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)
# Output: erry


##### 

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name): ##define function
  len1 = len(first_name) ##temp variable len1 equal to length of first name 
  len2 = len(last_name) ##temp variable len2 equal to length of last name 
  return first_name[len1-3:] + last_name[len2-3:] ##return last 3 letters of first name with last 3 letters of second name 

temp_password = password_generator(first_name, last_name) ##variable equal to call of the function 
print(temp_password) ## prints ikouki

####

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]  ##this prints t as it's the second to last 
final_word = company_motto[-4:] ##this prints otto as it prints the last 4 letters 

#####


####STRING IMMUTABLE. CANNOT CHANGE THE STRING, BUT CAN DO VIA CONCATENTATING 
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[-2:]
print(fixed_first_name)  ##prints Rob. 




