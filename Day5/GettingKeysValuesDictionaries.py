## can use built in list() function 

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

##  also have a keys() method 
# cannot be modified, just gives keys that can be iterated through 
for student in test_scores.keys():
 print(student)
 # prints 
#  Grace
# Jeffrey
# Sylvia
# Pedro
# Martin
# Dina

##

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users) ##prints the keys 
print(lessons) ##prints the keys for num_exercises 

## to get all values - can use values() built in function 

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
 print(score_list)
 ## will print 
#  [80, 72, 90]
# [88, 68, 81]
# [80, 82, 84]
# [98, 96, 95]
# [78, 80, 78]
# [64, 60, 75]

##  IF WANT TO LIST THE VALUE, CAN DO LIKE THIS 

list(test_scores.values())

##

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values(): #for loop iterating through exercises in num_exercises to get values 
  total_exercises += exercises #total exsercies to increase by exercises 
print(total_exercises) 
 
##### GET ALL ITEMS using items() method 
### CAN GET BOTH KEYS AND VALUES 

## EXAMPLE Syntax 

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items(): #for loop, iterating through company, and value in dictionary to get all items 
 print(company + " has a value of " + str(value) + " billion dollars. ") ## print name of company + str + value

# prints 
# Apple has a value of 184 billion dollars.
# Google has a value of 141.7 billion dollars.
# Microsoft has a value of 80 billion dollars.
# Coca-Cola has a value of 69.7 billion dollars.
# Amazon has a value of 64.8 billion dollars.

###
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for company, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + company + "s.")

##prints
# Women make up 28 percent of CEOs.
# Women make up 9 percent of Engineering Managers.
# Women make up 58 percent of Pharmacists.
# Women make up 40 percent of Physicians.
# Women make up 37 percent of Lawyers.
# Women make up 9 percent of Aerospace Engineers.

######

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + key + " is the " + value + " card.")
