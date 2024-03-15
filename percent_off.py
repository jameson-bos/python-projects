# User goes to the store, and sees 15 percent off of an item. User wants to know the final price of the item
# User also wants to know how much money they're saving. 

# discounted price = item cost - (item cost × percent off / 100)
# float(stringPercent.strip('%')) / 100.0
item_cost = input("Hello, what's the price of the item?")
item_cost = float(item_cost)
percent_off = input("\nGreat, and what's the percent off?")

if percent_off.isdigit():
    percent_off = float(percent_off.strip('%')) / 100.0
else:
    print('Please print a percent next time.')
    quit()

saved_money = percent_off * item_cost
discounted_price = (item_cost * percent_off) - item_cost
discounted_price = str(discounted_price)

print(f"\nThe final price of your item is ${discounted_price.strip('-')}.")
print(f"\nYou saved ${saved_money}, nice!")