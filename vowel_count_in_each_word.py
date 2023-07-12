s=input().split()
l=['a','e','i','o','u','A','E','I','O','U']
c=[]
for i in s:
    d=0
    for j in i:
        if j in l:
            d+=1
    c.append(d)
print(*c)    
        
        
        
        