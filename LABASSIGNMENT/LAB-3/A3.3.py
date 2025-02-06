def tree(n):
 sum=1
 for i in range(1,n+1):
        if i%2==1:
            sum*=2
        else:
            sum+=1
 print(sum)
test=int(input("enter no of test cases"))   
l=[]
for j in range(test):
    l.append(int(input("enter the no:")))  
j=0
for j in range(test):
    tree(l[j])                 