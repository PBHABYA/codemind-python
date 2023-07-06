n=int(input())
s=list(map(int,input().split()))
c=[]
d=[]
for i in s:
    if i not in c:
        c.append(i)
for j in c:
    if j%2==0:
        d.append(j)
print(sum(d))        
        