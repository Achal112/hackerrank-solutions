import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    res = numpy.array(arr[::-1], float)
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Input (stdin)
# 1 2 3 4 -8 -10
# Output
# [-10.  -8.   4.   3.   2.   1.]
