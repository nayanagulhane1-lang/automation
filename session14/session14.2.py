#Given a list of usernames from an Instagram-like app, use a list comprehension to 
# create a new list containing only those usernames that start with the letter 'a' or 'A'.
usernames = ['anita', 'Anjali', 'sonu', 'aachal', 'merry']

new_username = [username for username in usernames if username.startswith(('a', 'A'))]

print(new_username)
