import math
ab = int(input())
bc = int(input())
theta = math.atan2(ab, bc)
degree = math.degrees(theta)
print(str(round(degree)) + chr(176))
