
import math
points=[]
for _ in range(1,11):
    x,y,z= map(float,input("enter the coordinates").split(','))
    points.append((x,y,z))
    nearest_neighbors=[]
for i in range(len(points)):
    min=float('inf')
    nearest_neighbor=None
    for j in range(len(points)):
        if i!=j:
            distance = math.sqrt(
                (points[i][0] - points[j][0]) ** 2 +
                (points[i][1] - points[j][1]) ** 2 +
                (points[i][2] - points[j][2]) ** 2
            )
            if(distance<min):
                min=distance
                nearest_neighbor=points[j]
    nearest_neighbors.append((points[i], nearest_neighbor)) 
for point, neighbor in nearest_neighbors:
 print(f"Point: {point} -> Nearest Neighbor: {neighbor}")            

