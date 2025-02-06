def palindrome(word):
    if(word==word[::-1]):
        return 0
    else:
        return 1
def makepalindrome(word):
    reverse=list(word[::-1])
    word=list(word)
    cnt=0
    for i in range(len(word)):
            if(word[i]!=reverse[i]):
                 word[i]=min(word[i],reverse[i])
                 cnt+=1
            else:
                 continue
    print(cnt)      
test=int(input("enter no of test cases")) 
l=[] 
for i in range(test):
    l.append(input("enter the word:")) 
i=0
for i in range(test):
     if(l[i].isupper()):
          exit
     if(palindrome(l[i])):
          makepalindrome(l[i])
     else:
          print(0)
           
          

            
            

        