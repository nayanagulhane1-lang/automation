#Create a program that takes the price of a Zomato order as input (string), converts it to a float, adds a 10% delivery fee, and prints the final bill amount with two decimal places using f-string formatting.<br><br><em><strong>Hint:</strong> Use float() for conversion and format the output as Rs. 123.45.</em>

price=float(input("Enter zomato order price: "))
total_bill=price+price*10/100
print(f"final bill is Rs. {total_bill:.2f}.")