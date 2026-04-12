class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        self.current += 2
        return self.current - 2


class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        self.current += 2
        return self.current - 2


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    
    for _ in range(n):
        print(stream.get_next())
        
q = int(input())

for _ in range(q):
    stream_name, n = input().split()
    n = int(n)

    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())


# Input (stdin)
# 3
# odd 2
# even 3
# odd 5
# Output
# 1
# 3
# 0
# 2
# 4
# 1
# 3
# 5
# 7
# 9
