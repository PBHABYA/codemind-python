s=input().split()
c=""
d=[]
for i in s:
    if i.isupper or i.islower():
        c+=i
for i in c:
    a=ord(i)
    d.append(a)
l=min(d)
g=max(d)
o=chr(l)
p=chr(g)
c1=0
c2=0
for i in c:
    if o==i:
        c1+=1
    elif p==i:
        c2+=1
print(o,c1,p,c2)        
        
        
        

        