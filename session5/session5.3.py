#Given a list of cricket scores: [45, 67, 23, 89, 100], 
# use a for loop to calculate and print the total score.

cricket_scores = [45, 67, 23, 89, 100]

total = 0

for score in cricket_scores:
    total = total + score

print("Total score:", total)
