#Write a Python function get_unique_cuisines(restaurants) that takes a list of restaurant cuisines
# (e.g., ['Italian', 'Chinese', 'Italian', 'Mexican', 'Chinese']) and returns a set of unique cuisines 
# like Zomato shows in its filters.
list_of_restaurent=(['Italian', 'Chinese', 'Italian', 'Mexican', 'Chinese'])
def get_unique_cuisines(restaurants):
    return set(restaurants)
print(get_unique_cuisines(list_of_restaurent))
    