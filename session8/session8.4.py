#Given a list of strings representing Instagram usernames, 
# write a function filter_invalid_usernames(usernames) that returns a new list containing 
# only the usernames that are valid (use your validate_username function from Task 2).
def validate_username(username):
    if len(username) >= 5:
        return True
    else:
        return False
    
    
def filter_invalid_usernames(usernames):
    new_list = []

    for username in usernames:
        if validate_username(username):
            new_list.append(username)

    return new_list


usernames = ["nayana123", "abc", "ojasvi123", "xy", "testuser"]

print(filter_invalid_usernames(usernames))