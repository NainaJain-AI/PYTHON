def squareno(a,b):
    cnt=0
    for i in range(a,b+1):
        temp=i**0.5
        if(temp.is_integer()):
            cnt+=1
        else:
            continue
    print(cnt)
test=int(input("enter no of test cases"))   
l=[]
for i in range(test):
    a,b= map(int,input().split())
    t=(a,b)
    l.append(t)
i=0
for i in range(test):
    squareno(l[i][0],l[i][1])
                
