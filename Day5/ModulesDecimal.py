##using decimal method helps to format numbers more accurately. 

from decimal import Decimal

cost_of_gum = Decimal('0.10')  ##by setting 0.10
cost_of_gumdrop = Decimal('0.35') ##with 0.35 - this sets the decimals we will want to use 

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996

####

from decimal import Decimal

a = Decimal("10.55")
b = Decimal("2.3")

# Addition
print(a + b)  # Output: 12.85 # 2 places

# Subtraction
print(a - b)  # Output: 8.25 #2 places 

# Multiplication
print(a * b)  # Output: 24.265 #

# Division
print(a / b)  # Output: 4.586956521739130434782608696

####

from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal("0.2") + Decimal("0.69")
print(two_decimal_points)  ##prints 0.89

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points) ##prints 0.3445

