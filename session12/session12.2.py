#Create a function named format_follower_count that takes a number and 
# returns a string formatted like Instagram (e.g., 1500 becomes '1.5K', 1200000 becomes '1.2M'). 
# Test your function with 950, 1500, and 1200000.<br><br><em><strong>Hint:</strong>
# Use conditional statements to check the size and format accordingly.</em>

def format_follower_count(number):
    if number>=100000:
        return str(number/100)+"M"
    elif number>=1000:
        return str(number/1000)+"K"
    else:
        return str(number)
print(format_follower_count(950))
print(format_follower_count(1500))    
print(format_follower_count(1200000)) 