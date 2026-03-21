an = int(input())
a = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    op, _ = input().split()
    others = set(map(int, input().split()))
    getattr(a, op)(others)

print(sum(a))
