#case study1
t=int(input())
j=0
for j in range(t):
    n,x,s= map(int,input().split())

 
    for i in range(s):

     a,b= map(int,input().split())
    
     if a>n or b>n :
         print("incorrect value ")
     if x==a :
         a=a+b
         b=a-b
         a=a-b
         x=a
     elif x==b:
         a=a+b
         b=a-b
         a=a-b
         x=b
     else:
         print("incorrect swap ")  
print(x)        


