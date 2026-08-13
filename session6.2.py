#Simulate a Zomato-style order retry: Use a while loop to keep asking the user to enter 
# 'yes' to confirm their food order, and stop only when the user types 'yes'.

order=input("confirm your food order(yes/no): ")

while order!="yes":
    order=input("please enter yes to confirm your order: ")
print("order confirmed")    
