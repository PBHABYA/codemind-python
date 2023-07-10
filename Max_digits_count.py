n=int(input())
s=list(map(int,input().split()))
d=[]
for i in s:
    i=str(i)
    a=len(i)
    d.append(a)
m=max(d)
c=0
for i in s:
    i=str(i)
    a=len(i)
    if a==m:
        c+=1
print(c)        
