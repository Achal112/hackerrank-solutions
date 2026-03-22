from itertools import combinations

# Input
n = int(input())
letters = input().split()
k = int(input())

# Total combinations
total = list(combinations(range(n), k))

# Count combinations with at least one 'a'
count = 0

for combo in total:
    if any(letters[i] == 'a' for i in combo):
        count += 1

# Probability
probability = count / len(total)

print(round(probability, 4))

# Input (stdin)
# 4
# a a c d
# 2
# Output
# 0.833333333333
