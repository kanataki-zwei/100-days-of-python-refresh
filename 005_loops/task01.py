scores = [150,150,130, 200, 500, 1000]
sum_of_scores = sum(scores)
print(sum_of_scores)

# using loops to get sum
sum = 0
for score in scores:
    sum+=score
print(sum)

# using loops to get max
max_score = scores[0]
for score in scores[1:]:
    if score > max_score:
        max_score = score
print(max_score)