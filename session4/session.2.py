#Build a Flipkart-style discount calculator: input the original price and discount percentage, 
# then use arithmetic operators to calculate and print the final price after discount.

price=float(input("Enter orignal price: "))
discount=float(input("Enter discount percentage: "))
discount_amount=price*discount/100
final_price=price-discount_amount
print(final_price)
