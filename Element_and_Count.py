n=int(input())
s=list(map(int,input().split()))
c=[]
d=[]
for i in s:
    if i not in c:
        c.append(i)
for i in c:
    d.append(i)
    d.append(s.count(i))
print(*d)    
    
    