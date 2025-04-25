import numpy as np
import math
def polar(arr):
    angle=math.degrees(math.atan(arr[1]/arr[0]))
    arr=np.square(arr)
    magnitude=math.sqrt(np.sum(arr))
    polar_cordinates=(magnitude,angle)
    print(polar_cordinates)
n=int(input("N:"))
coordinates=np.array([input("").split() for i in range(n)])
for arr in coordinates:
    polar(arr.astype(int))