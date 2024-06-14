def username_generator(first_name, last_name): ##define function
  if len(first_name) < 3: ##if length of first name less than 3
    first = first_name  # use name 
  else:
    first = first_name[:3] ##else use first 3 letters of first name 

  if len(last_name) < 4: ## if length of last name less than 4 
    second = last_name  ##use last name 
  else:
    second = last_name[:4] ##else use first 4 letters 

  user_name = first + second  ##username set and returned 
  return user_name

user = username_generator("Deepak", "Hussain") ##variable set equal to call of function 
print(user) ##prints DeeHuss

#####

def password_generator(user_name):  ##defines function
    password = ""  ##empty password string
    for i in range(0, len(user_name)): #for loop, checking index in range (from 0, through length of username)
        password += user_name[i-1] ##password + username index -1
    return password ##return password

print(password_generator("Hugger"))  ##rHugge
  
