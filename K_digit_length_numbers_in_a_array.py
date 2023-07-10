a,b=map(int,input().split())
s=list(map(int,input().split()))
l=0
for i in s:
    if i<0:
        i=-i
    i=str(i)
    c=len(i)
    if b==c:
        l+=1
print(l)        