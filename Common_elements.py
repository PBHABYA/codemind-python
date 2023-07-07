n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
e=[]
for i in a:
    if i not in c:
        c.append(i)
for i in b:
    if i not in d:
        d.append(i)
for i in c:
    if i in d:
        e.append(i)
print(*e)        