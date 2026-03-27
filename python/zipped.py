n, x = map(int, input().split())
mark = []
for _ in range(x):
    mark.append(list(map(float, input().split())))
    
for i in zip(*mark):
    avg = sum(i)/x
    print(avg)


# Input (stdin)
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86
# 91 92 83 89 90.5
# Output
# 90.0
# 91.0
# 82.0
# 90.0
# 85.5
