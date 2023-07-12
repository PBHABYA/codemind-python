s=input()
x=['a','e','i','o','u','A','E','I','O','U']
c=[]
d=[]
for i in s:
    if i in x:
       c.append(i)
for i in c:
    if i not in d:
        d.append(i)
        
print(*d)       
        
        
        