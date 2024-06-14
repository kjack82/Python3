hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price #adds prices together
print(total_price)
  
average_price = total_price / len(prices) #total price / length of prices list 
print(average_price)

new_prices = [price - 5 for price in prices] #take 5 off every price in prices list
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):  #for loop that goes from 0 to end of hairstyeles list
    total_revenue += prices[i] * last_week[i]  #adding price x amount of times last week had that hairstyle to total revenue 
print(total_revenue)

average_daily_revenue = total_revenue / 7 #total revenue / 7 for number of days 
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30] #going through each index from 0 -end of length to display those that are under 30 
print(cuts_under_30)