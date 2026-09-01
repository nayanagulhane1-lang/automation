#Build a function called get_discounted_price that takes the original price and
# a discount percentage, and returns the final price after applying the discount. 
# Use this to calculate the final price for an item costing 999 with a 20% discount.

def get_discounted_price(price,disc_percentage):
    final_price=price*20/100
    return final_price
print(get_discounted_price(999,20))
