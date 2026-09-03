#Create a list of the prices of 5 food items as integers, then use a list comprehension 
# to generate a new list that adds 18% GST to each price and print the result.

prices = [100, 200, 300, 400, 500]

gst_prices = [price * 1.18 for price in prices]

print(gst_prices)
