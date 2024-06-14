# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)

print(25 * 68 + 13 / 28) #can put within brackets and calc will be done)

coffee_price = 1.50  #can assign variable to an integer or float
number_of_coffees = 4

# Prints "6.0"
print(coffee_price * number_of_coffees) #can then do same calc as would do if had not assigned variables 
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

# Updating the price 
coffee_price = 2.00

# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)

#the variable will not change unless = sign used, total will only change if variable reassigned 

quilt_width = 8
quilt_length = 12

print(quilt_width * quilt_length)

quilt_length = 8

#exposnents  ie power of. These take precedent before other cals and use **

# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6? Ie 6 x 6 x 6 x 6 
print(6 ** 4 )

#modulo operator is % 
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

order_263_r = 263 % 11
print(order_263_r)
order_263_coupon = "no"

order_264_r = 264 % 11
print(order_264_r)
order_264_coupon = "yes"

