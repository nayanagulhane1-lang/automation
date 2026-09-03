#Given a nested list where each sublist contains the ratings (1-5) 
# for a Zomato restaurant from different users, use a nested list comprehension 
# to flatten the list and filter out all ratings below 3.
ratings = [
    [5, 2, 4],
    [1, 3, 5],
    [2, 4, 1]
]

result = [rating for sublist in ratings for rating in sublist if rating >= 3]

print(result)
