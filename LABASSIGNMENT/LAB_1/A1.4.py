l0=[]
l1=[]
l2=[]
l3=[]
l4=[]
li=[]
for i in range(1,1001):
 li.append(i)
 match i%5:
        case 0:
            l0.append(i)
        case 1:
            l1.append(i)
        case 2:
            l2.append(i)
        case 3:
            l3.append(i)
        case 4:
            l4.append(i)   
l=l0 +l1+l2+l3+l4 
l=set(l)
li=set(li)
if(l==li) :
    print("valid")
else:
    print("invalid")

       
