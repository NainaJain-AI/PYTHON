string='absfdeabbasu'
substring='ab'

for i in range(len(string)-len(substring)+1):
    if string[i:i+len(substring)]==substring:
        rindex=i
print(rindex)        
