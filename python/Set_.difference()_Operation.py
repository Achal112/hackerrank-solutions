eng_sub = int(input())
roll_eng_sub = set(map(int, input().split()))
french_sub = int(input())
roll_french_sub = set(map(int, input().split()))
print(len(roll_eng_sub.difference(roll_french_sub)))

# Input (stdin)
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Output
# 4
