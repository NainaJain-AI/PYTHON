import re
text=input("enter the text:")
text=text.lower()
l=[]
for i in text:
     l+=re.findall("[a-z]+",i)     
l=set(l)
if(int(len(l))==26):
    print("panagram")
else:
      print("not panagram")   