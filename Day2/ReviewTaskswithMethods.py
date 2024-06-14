inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len) #outputs length

first = inventory[1]
print(first) #prints first item

last = inventory[-1]
print(last)  #prints last items 

inventory_2_6 = inventory[2:6]
print(inventory_2_6) #prints from items 2 - to 5

first_3 = inventory[:3]
print(inventory_2_6)   #prints first 3 items 

twin_beds = inventory.count("twin bed")
print(twin_beds)  #counts number of twin beds 

removed_item = inventory.pop(4)
print(removed_item)  #removes 5th element 

inventory.insert(10, "19th Century Bed Frame")
print(inventory)   #inserts bed frame to the list in 11th position 