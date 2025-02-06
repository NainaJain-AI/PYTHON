def sum(n):
    sum=0
    while n!=0:
        i=n%10
        sum+=i
        n=n//10
    return sum
n=int(input("enter the no:"))
while n>9:
    n=sum(n)
print(n)        