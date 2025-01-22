import random
l=[]
count=0
for i in range(100):
   n=random.randint(0,1)
   l.append(n)
   if not n:
      count+=1
print(count) 
  


