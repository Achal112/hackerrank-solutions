if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    score = list(set(arr))
    
    score.sort()

    runner_up = score[-2]
    print(runner_up)
