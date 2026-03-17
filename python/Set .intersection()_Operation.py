n = int(input())
n_roll_no = set(map(int, input().split()))
b = int(input())
b_roll_no = set(map(int, input().split()))
print(len(n_roll_no.intersection(b_roll_no))) 

# Input (stdin)
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Output
# 5
