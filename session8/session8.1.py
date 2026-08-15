#Write a Python function is_valid_email(email) that checks if a given string is a valid email address 
# using string methods (like find, count, startswith, endswith) and returns True or False.
# <br><br><em><strong>Hint:</strong> Check for exactly one '@', at least one '.', and that '@' 
# is not at the start or end.</em>
    
def is_valid_email(email):
    if email.count("@") == 1 and "." in email and not email.startswith("@") and not email.endswith("@"):
        return True
    else:
        return False


print(is_valid_email("test@gmail.com"))
print(is_valid_email("@gmail.com"))
print(is_valid_email("test@gmail"))
