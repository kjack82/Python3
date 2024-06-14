train_mass = 22680  ##VARIABLES DEFINED 
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8


# Write your code below: 
def f_to_c(f_temp):  ##FUNCTION DECLARED WITH FARENHEIT AS PARAM
  c_temp = (f_temp - 32) * 5/9 ##VARIABLE OF CELC EQUAL TO FAREN - 32 * 5/9
  return c_temp  ##RETURNS CELC

f100_in_celcius = f_to_c(100) 

print(f100_in_celcius)## RETURNS 37.77

def c_to_f(c_temp):  ##NEW FUNCTION DECLARED , CELC AS PARAM
  f_temp = c_temp * (9/5) + 32  ##FAREN EQUAL TO CELC * 9/5 + 32 
  return f_temp  #RETURNS FAREN 

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)  ##RETURNS 32 


### 


def get_force(mass, acceleration):  ##DEFINES NEW FUNCTION WITH MASS, ACCEL AS PARAMS 
  return mass * acceleration  ##RETURNS MASS * ACCEL

train_force = get_force(train_mass, train_acceleration)  ##NEW VARIABLE DEFINED, EQUAL TO CALLING OF ABOVE FUNCTION WITH ARGUEMENTS DEFINED 
print(train_force) ##PRINTS 226800

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c):  ##NEW FUNCTION DECLARED WITH MASS AND C AS PARAMS - C ALREADY DEFINED 
  return mass * (c*c)  ##RETURNS MASS * C SQUARED 

bomb_energy = get_energy(bomb_mass, c)  ##VARIABLE EQUAL TO CALLING OF FUNCTION WITH ARGUEMENTS DEFINED 

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")  ##PRINTS 90000000000000

def get_work(train_mass, train_acceleration, train_distance):  ##NEW FUNCTION DECLARED WITH ARGUEMENTS AS ALREADY DEFINED 
  return get_force(train_mass, train_acceleration) * train_distance  ##RETURNS CALLING OF PREVIOUS FUNCTION GET FORCE * FISTANCE 

train_work = get_work(train_mass, train_acceleration, train_distance) ##NEW VARIABLE IS EQUAL TO CALLING OF GET WORK FUNCTION 

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")  ##PRINTS 22680000 JOULES 