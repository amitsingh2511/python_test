def compute_matches(teamA, teamB):
    matches = []
    for x in teamB:
        count = 0
        for y in teamA:
            if y <= x:
                count += 1
        matches.append(count)
    return matches

# teamA = [1, 2, 3]
# teamB = [2, 4]
teamA = [2, 10, 5,4,8]
teamB = [3,1,7,8]
result = compute_matches(teamA, teamB)
print(result)

# when input given for teamA = [1,2,3] and teamB = [2,4]
# Output come like [2,4]

# when input given for teamA = [2, 10, 5,4,8] and teamB = [3,1,7,8]
# Output come like [1,0,3,4]