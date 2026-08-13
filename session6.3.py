#Build a Flipkart-style cart total calculator: Given a list of item prices, 
# use a while loop to sum the prices until the total exceeds 1000, then stop and print the subtotal.
# <br><br><em><strong>Hint:</strong> Use loop control statements to exit the loop once the subtotal 
# goes above 1000.</em>

item_per_price=[200,300,400,500]
sum=0
i=0

while sum<1000:
     sum=sum+item_per_price[i]
     i=i+1
     
     if sum>1000:
       break
print(sum)