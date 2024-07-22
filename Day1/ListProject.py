## creating a new list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

##creating a second list
prices = [2, 6, 1, 3, 2, 7, 2]

## count method used to count how many times 2 appears 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices) ## prints 3

## len method to give the length of the pizza toppings list
num_pizzas = len(toppings)
print(num_pizzas) ## prints 7

print("We sell " + str(num_pizzas) + " different kinds of pizza!, where " + str(num_pizzas) + " represents the value of our variable num_pizzas")

## creating a new 2d list storing toppings and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

## sort method used to sort list from cheapest price upwards
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

## method to get last item from the list 
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

## method to remove last item 
pizza_and_prices.pop()
print(pizza_and_prices)

## method used to insert new data in position 4. 
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

## method used to pull the first three items from 2d list 
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest) 