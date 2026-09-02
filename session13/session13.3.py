#Write a lambda function to filter out all songs longer than 4 minutes from a list of tuples
# representing Spotify songs (each tuple contains song name and duration in minutes).

songs = [
    ("Song A", 3.5),
    ("Song B", 4.5),
    ("Song C", 3.8),
    ("Song D", 5.2)
]

long_songs = list(filter(lambda song: song[1] > 4, songs))

print(long_songs)
