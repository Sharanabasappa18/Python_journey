import re
s1 = "The BodyGuard is the best album"
s2="Avengers endgame is te best movie"
# the pattern to search for
pattern = r"games"
pattern2=r"is"
# Use the search() function to search for the pattern in the string
result = re.search(pattern2, s2)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")
