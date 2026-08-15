#Create a function validate_userna:me(username) that returns True only if the username 
# is at least 6 characters, contains only letters and numbers, and does not start with a digit.
def validate_username(username):
    if len(username)>=6 and username.isalnum()and not username[0].isdigit():
        return True
    else:
        return False
    
print(validate_username("Nayana"))  
print(validate_username("Nayana123"))   # True
print(validate_username("Nay12"))       # False
print(validate_username("123Nayana"))   # False
print(validate_username("Nayana@123"))  # False  