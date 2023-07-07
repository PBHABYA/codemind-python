a,b=map(int,input().split())
s=list(map(int,input().split()))
c=0
for i in s:
    if i%b==0:
        c+=1
print(c)        