
def append_size(my_list):
  my_list.append(len(my_list))  ##my list to add on the length of my list
  return my_list ##return updated list

print(append_size([23, 42, 108]))  ## returns 23, 42, 108, 3

####

#Write your function here
def append_sum(my_list): #define function
  my_list.append(my_list[-1] + my_list[-2])  #my list to add on the result of the last and second last numbers in list
  my_list.append(my_list[-1] + my_list[-2])##do this 3 times 
  my_list.append(my_list[-1] + my_list[-2])
  return my_list #return updated list 

print(append_sum([1, 1, 2]))  ##returns [1, 1, 2, 3, 5, 8]]
 ######
 
def larger_list(my_list1, my_list2):  #define new function
  if len(my_list1) > len(my_list2):  #if length of list 1 is greater than len of list2
    return my_list1[-1]  #return last item in list 1
  elif len(my_list2) > len(my_list1):  #if length of list 2 is greater than length of list 1
    return my_list2[-1] #return end item from list 2
  else:   #otherwise 
    return my_list1[-1]  #end of list 1

#####

def more_than_n(my_list, item, n):  #define function
  if my_list.count(item) > n:   ##if count of items within my list is greater than n
    return True  ##return true 
  else:  #otherwise
    return False  ##return false 

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#######

def combine_sort(my_list1, my_list2): ##defines function with two lists as params
  return sorted(my_list1 + my_list2) ##return a sorted list of the 2 lists added together 

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))  ##prints [-10, 2, 2, 4, 5, 5, 10, 10]


 