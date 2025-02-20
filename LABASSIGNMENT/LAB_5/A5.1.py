a=int(input())
b=int(input())
m=0
for i in range(a,b+1):
 for j in range(a,b+1):
   xor=i^j
   m=max(m,xor)
print(m) 