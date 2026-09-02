#Define a function called apply_coupon that takes an order total and an optional coupon code argument 
# (default is None). If the coupon code is 'SAVE10', apply a 10% discount; 
# otherwise, return the original total.
coupon_code='SAVE10'
def apply_coupon(order_total, coupon_code=None):
     if coupon_code=='SAVE10':
         order_total=order_total*0.90
         
         return order_total
     else:
         return order_total
print(apply_coupon(560,'SAVE10'))     