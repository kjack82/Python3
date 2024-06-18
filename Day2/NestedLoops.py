project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  print(team)
  #prints out 
# ["Ava", "Samantha", "James"]
# ["Lucille", "Zed"]
# ["Edgar", "Gabriel"]

#to list the individual names, need to do the following

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student) # outputs each individual name 
    
    
    
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0 
for location in sales_data:  #location is temp variable 
  print(location) #prints each nested list 
  for sales in location: #sales new temp variable and iterates through each item within each nested array 
    scoops_sold += sales  #this accumulates the sales 

print(scoops_sold) #prints total amount of ales at 96 
    
#####

groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)
