# reverse of a no
number=int(input("enter the number "))
sum=0

while number!=0:
    i=number%10
    sum=sum*10+i
    number//=10
print("reverse no is",sum)    