#Similar to a list. However once created, it cannot be changed. 

my_info = ('Kate', 42, 'Programmer')
print(my_info)
print(my_info[1])

#can interact to get data. But cannot change data, cannot re-order, add, remove etc. 
#need an immutable data structure. 

#set variables
name, age, occupation = my_info
print(name) #prints Kate 
## this is referred to as unpacking a tuple
#if only want 1 item, must add a trailing comma 
#used to sotre a list of differnt data, eg as above, info is different, but all data is relating to me.

#generally use lists when info is similar. Tuples for different data that does not need to be changed. 