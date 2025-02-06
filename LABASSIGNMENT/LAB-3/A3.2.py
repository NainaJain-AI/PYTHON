def isfibo(n):
    temp1=(5*n*n+4)**0.5
    temp2=(5*n*n-4)**0.5
    if temp1.is_integer() or temp2.is_integer():
        print("IsFibo")
    else:
        print("IsNotFibo")    
test=int(input("enter no of test cases"))   
l=[]
for i in range(test):
    l.append(int(input("enter the no:")))  
i=0
for i in range(test):
    isfibo(l[i])       
    