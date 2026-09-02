#Write a Python function called calculate_discounted_price that takes two arguments:
# price and discount_percent, and returns the final price after applying the discount.
def calculate_discounted_price(price,dis_percentage):
    final_price=price*dis_percentage/100
    return final_price
print(calculate_discounted_price(300,10))
