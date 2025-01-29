word=input("enter the word:")
new_word=""
for i in range(len(word)):
  if i%2:
    new_word+=word[i].upper()
  else:
    new_word+=word[i]
print(new_word)  
  