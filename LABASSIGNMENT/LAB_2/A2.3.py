cases=int(input(""))
count=[]
for i in range(cases):
    num=input("")
    count.append(0)
    for digit in num:
        if digit!='0':
            if int(num) % int(digit)==0:
                count[i]+=1
for j in range(cases):
    print(count[j])            
    
    

    
    
    
    