t = int(input())

for _ in range(t):
    a = int(input())
    a_ele = set(map(int, input().split()))
    b = int(input())
    b_ele = set(map(int, input().split()))
    
    print(a_ele.issubset(b_ele))

# Input-
# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Output-
# True 
# False
# False
