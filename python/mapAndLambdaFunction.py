cube = lambda x: x * x * x# complete the lambda function 

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    # return a list of fibonacci numbers
    return fib[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Input (stdin)
# 5
# Output
# [0, 1, 1, 8, 27]
