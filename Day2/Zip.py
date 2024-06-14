#USe to combine two associated data sets together. 

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights) #would print <zip object at 0x7f1631e86b48> --- needs to be converted to a list 
converted_list = list(names_and_heights)
print(converted_list)  #prints [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]

# note converted to a tuple (the inner list)

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

#prints [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]