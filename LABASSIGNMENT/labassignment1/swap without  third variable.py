#swap without using third variable

a=int(input("enter value of a"))
b=int(input("enter value of b"))
print("before swap a= ",a)
print("before swap b= ",b)
a=a+b
b=a-b
a=a-b
print("after swap a= ",a)
print("after swap b= ",b)