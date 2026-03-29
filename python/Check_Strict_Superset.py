a = set(map(int, input().split()))
n = int(input())
res = True
for _ in range(n):
    other = set(map(int, input().split()))
    if not a.issuperset(other):
        res = False
print(res)

# Input (stdin)
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Output
# False
