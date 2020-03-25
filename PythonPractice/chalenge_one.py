challenge_list = [1, 8, 5, 2, 8, 5, 1]  # remove duplicates challenge with list
blank = []

for x in challenge_list:
    if x in blank:
        challenge_list.remove(x)
    blank.append(x)
print(blank)
print(challenge_list)