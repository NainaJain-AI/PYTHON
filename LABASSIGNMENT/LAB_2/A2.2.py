choice=1
product={}
while choice:
    name=input("enter product name")
    price=float(input("enter product price"))
    product[name]=price
    choice=int(input("enter 1 for yes or 0 for no"))
choice=1
while choice:
 name=input(" product name") 
 if name in product:
    print("price is",product[name]) 
choice=int(input("enter 1 for yes or 0 for no"))  
    
    