menu = {"Pizza": 2.99, "Burger": 3.99, "Hot dog": 1.99, "Cheese": 0.59, "Ice cream": 1.49, "Churro": 0.79, "Soda": 0.89}

def total_price(item1, item2):
    completePrice = menu[item1] + menu[item2]
    
    return completePrice
    

print(total_price("Pizza","Burger"))

def price_difference(item1, item2):
    if menu[item1] > menu[item2]:
        difference = menu[item1] - menu[item2]
    else:
        difference = menu[item2] - menu[item1]
    return difference
    
print(price_difference("Pizza","Burger"))

def inflation(item1):
    inflated_price = menu[item1] * 1.10
    return inflated_price

print(inflation("Pizza"))

def deflation(item2):
    deflation_price = menu[item2] * .9
    return deflation_price
print(deflation("Burger"))
    
#a friend gave you 2 dollars so you can buy whatever you want and lets you keep the change
def friend(item1):
    money_friend = menu[item1] - 2
    return money_friend
print(friend("Ice cream"))


   




