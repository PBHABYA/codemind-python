n=int(input())
s=list(map(int,input().split()))
a=[]
for i in s:
    i=str(i)
    b=len(i)
    a.append(b)
n=min(a)
c=0
for i in s:
    i=str(i)
    b=len(i)
    if b==n:
        c+=1
print(c)        
        