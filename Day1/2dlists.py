#can put lists within lists 

# heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]

tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
sams_height = heights[2][1] #0,0 for Jenny, 0,1 for 61, 1, 0 for Alexus, 1, 1 for 67 and so on 
print(sams_height)

ages = [["Aaron", 15], ["Dhruti", 16]]


class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2] [1]
print(sams_score)

ellies_score = class_name_test[-1][-1] #using -1 for each woill take the last ones from end of list 
print(ellies_score)


class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
class_name_hobbies[0][1] = "Meditation" #updates Jenny's hobby
print(class_name_hobbies) 
class_name_hobbies[-1][-1] = "Football" #can use negative indices too
print(class_name_hobbies)


incoming_class = [
  ["Kenny", "American", 9],
  ["Tanya", "Ukrainian", 9],
  ["Madison", "Indian", 7]
  ]
print(incoming_class)

incoming_class[2][2] = 8 #changes grade for Madison
print(incoming_class)

incoming_class[-3][-3] = "Ken" #changes name ofr Kenny to Ken, using negative indices 
print(incoming_class)



first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

preferred_size.append("Medium") #adding medium to the end 
print(preferred_size)

customer_data = [    #new list
  ["Ainsley", "Small", True],
  ["Ben", "Large", False],
  ["Chani", "Medium", True],
  ["Depak", "Medium", False]
]
print(customer_data)

customer_data[2][2]=False  #changing Chani to false 

customer_data[1].remove(False)  #removng false for Ben 

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]  #adding new people and info to the list with a new list 
print(customer_data_final)  