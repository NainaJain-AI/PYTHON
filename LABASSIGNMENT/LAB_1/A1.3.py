
n=float(input("enter feet:"))
l=[12,3,5280,304.8,30.48,0.3048,0.0003048]
print("1=in inches\n2=yards\n3= miles\n 4= millimeters\n5= centimeters\n6=meters\n6= kilometers\n")
i=int(input("enter choice:"))
i-=1
if(i==1 or i==2 ):
    print(n/l[i])
else:
    print(n*l[i])    