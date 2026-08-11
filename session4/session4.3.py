#Create a Python program that checks if a Zomato order is eligible for free delivery:
# if the total amount is greater than or equal to 299, print 'Free Delivery', else print 'Delivery Charges 
# Apply'.
total_amount=int(input("Enter total amount: "))
if total_amount>=299:
    print("Free delivery")
else:
    print("Delivery charges apply")    
