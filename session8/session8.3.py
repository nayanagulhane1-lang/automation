#Build a password strength checker function check_password_strength(password) that returns 
# 'Weak', 'Medium', or 'Strong' based on these rules: Weak if less than 6 characters, 
# Medium if at least 6 and contains letters and numbers, Strong if it also contains at least
# one special character (!@#$%^&*).

def check_password_strength(password):
    if len(password)<6:
        return "Weak"
    if password.isalnum():
        return "Medium"
 
    return "Strong"
    
   
print(check_password_strength("6676"))
print(check_password_strength("abc123"))
print(check_password_strength("abc123@")) 


        
