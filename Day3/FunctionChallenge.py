def tenth_power(num):
  return num ** 10  ##return num to the power of 10 

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

####

def square_root(num):
  return num ** 0.5 ## return the square root of 

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

###

def win_percentage(wins, losses): 
  total_games = wins + losses ##total games is sum of wins and losses
  ratio_wins = wins / total_games ## wins / total games gives ratio of wins 
  ratio_percentage = ratio_wins * 100 ## converts to percentage 
  return ratio_percentage ##return percentage 

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

####

def average(num1, num2): 
  sum = num1 + num2 ## veraible set to add 1 + 2 
  return sum / 2 ##returns total / 2 as 2 inputs 

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

#####

def remainder(num1, num2):
  sum1 = num1 * 2 ##num1 x 2
  sum2 = num2 / 2 ##num2 / 2
  sum3 = sum1 % sum2 ## looking for remainder of sum1 / sum2
  return sum3

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))

##notecan do this in a more simple way 
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)


######
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

###################

def tip(total, percentage):
  return (total * percentage) / 100

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

#######################

def introduction(first_name, last_name):
  return last_name + ', ' + first_name + " " + last_name

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

#########

def dog_years(name, age):
  return name + ", you are " + str(age * 7) + " years old in dog years"

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

###########

def lots_of_math(a, b, c, d):
  sum1 = a + b
  print(sum1)
  sum2 = c - d
  print(sum2)
  sum3 = sum1 * sum2
  print(sum3)
  return sum3 % a

print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
