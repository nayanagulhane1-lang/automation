#Create a function called format_follower_count that takes a follower count as an argument and 
# returns the count formatted like Instagram (e.g., 1500 as '1.5K', 1200000 as '1.2M
# ').<br><br><em><strong>Hint:</strong> 
# Use conditional logic to determine which suffix to use based on the count.</em>

def format_follower_count(follower_count):
    if follower_count >= 1000000:
        return str(round(follower_count / 1000000, 1)) + "M"
    elif follower_count >= 1000:
        return str(round(follower_count / 1000, 1)) + "K"
    else:
        return str(follower_count)


print(format_follower_count(950))
print(format_follower_count(1500))
print(format_follower_count(1200000))
    
