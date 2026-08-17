#Build a function remove_duplicates(usernames) that takes a list of Instagram usernames
# and returns a new list with duplicates removed, preserving the original order.
# <br><br><em><strong>Hint:</strong> Use a loop and a temporary list to track seen usernames.
# </em>
usernames = ["nayana", "ojasvi", "nayana", "test", "ojasvi"]
def remove_duplicates(usernames):
    new_list=[]
    for username in usernames:
          if username not in new_list:
              new_list.append(username)
    return new_list    


usernames = ["nayana", "ojasvi", "nayana", "test", "ojasvi"]
print(remove_duplicates(usernames))
