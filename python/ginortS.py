s = input().strip()
def sort(ch):
    if ch.islower():
        return (0, ch)
    elif ch.isupper():
        return (1, ch)
    elif ch.isdigit():
        if int(ch) % 2:
            return (2, ch)
        else:
            return (3, ch)
            
res = ''.join(sorted(s, key = sort))
print(res)

# Input (stdin)
# Sorting1234
# Output
# ginortS1324
