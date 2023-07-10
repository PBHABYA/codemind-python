n=int(input())
s=list(map(int,input().split()))
d=[]
e=[]
for i in s:
    i=str(i)
    a=len(i)
    d.append(a)
m=max(d)
for i in s:
    i=str(i)
    a=len(i)
    if a==m:
        e.append(int(i))
print(*e)     