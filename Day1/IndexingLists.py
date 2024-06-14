employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employee_four)

print(employees[6])

#always starts with a 0

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

print(shopping_list[-1])  #this gives the last item within the list

last_element = shopping_list[-1]

index5_element = shopping_list[5]
print(index5_element)


garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

garden_waitlist[1] = "Calla" #replacing Adam with Calla using index
print(garden_waitlist)

garden_waitlist[-1] = "Alex" #replacing Alisha with Alex using negative index (to take from end)
print(garden_waitlist)

# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Remove a element
shopping_line.remove("Chris")
print(shopping_line)

#outputs ["Cole", "Kip", "Sylvana", "Chris"]  - only the first instance of Chris is removed. 

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)

order_list.remove("Flatbread")
print(order_list) #removes flatbread

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)

new_store_order_list.remove("Mango")
print(new_store_order_list) #removes first mango from list