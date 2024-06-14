# A loop that never terminates is called an infinite loop. These are very dangerous for our code because they will make our program run forever and thus consume all of your computer’s resources.

# A program that hits an infinite loop often becomes completely unusable. The best course of action is to avoid writing an infinite loop.

#can use cntr + c to stop an infinite loop 

# using a break 

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

print("End of search!")


dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption: 
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break


#USE OF CONTINUE

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)
  
  #prints
# 1
# 2
# 4
# 5
# 2

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
  
  



