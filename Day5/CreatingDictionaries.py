## dictionary is an unordered set of key: value pairs 

## EG want to sotre prices of items sold in  cafe 

menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
##dictionary is called menu 
## begins and ends with curly braces {}
## a key followed by : then value 


sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors) ##prints {'living room': 21, 'kitchen': 23, 'bedroom': 20, 'pantry': 22}

## can use numbers with numbers too
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

## can use another dictionary as the value associated with a key 

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

##can mix and match too 

person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}



### Keys can only be a string or a number, it cannot be a lst itself or dictionary 
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

## can create an empty dictionary 

empty_dict = {}

## can add to a dictionary with a single key:value pair 
## dictionary[key] = value

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# if want to add an item 
menu["cheesecake"] = 8
## menu now looks like
# {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

##prints {'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}

## can use .update() method if want to add more than 1 key value pair at a time 

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
## prints {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids) ## {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

## can overwrite a value 

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5 ##to change number from 3 to 5 
print(menu) # prints {"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis" ##adds the key value pair
oscar_winners["Best Picture"] = "Moonlight"  ## updates best picture 
print(oscar_winners)## {'Best Picture': 'Moonlight', 'Best Actor': 'Casey Affleck', 'Best Actress': 'Emma Stone', 'Animated Feature': 'Zootopia', 'Supporting Actress': 'Viola Davis'}

## can put lists together to combine a dictionary using comprehension 

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

## zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

# Takes a pair from the iterator of tuples
# Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# Creates a key : value item in the students dictionary
# Repeats steps 1-3 for the entire iterator of pairs

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine) ##zips the elements from each list and results in an iterator of tuples, each contsaining one from each lisy
drinks_to_caffeine = {key:value for key, value in zipped_drinks}  ##creates a dictionary comprehension that goes through tuples and creates key value pairs in dictionary 
print(drinks_to_caffeine)  ##{'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}
 ####
 
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)} ##zips two otgether in to disctionary 
print(plays)
plays.update({"Purple Haze": 1}) ## adds new entries 
plays["Respect"] = 94 ##overwrites entry
print(plays) ## {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 89, 'Good Vibrations': 5}
# {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}


library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library) # {'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}, 'Sunday Feelings': {}}

