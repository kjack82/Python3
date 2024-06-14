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




