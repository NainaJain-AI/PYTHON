test=int(input())
num=input()
l=num.split(" ")
if (len(l)!=test):
  print("ERROR")
  exit()
for k in l:
    k=int(k)
    if(k%2):
     k=(k+1)//2
     print(k*(k-1))
    else:
     k//=2
     print(k**2) 

   