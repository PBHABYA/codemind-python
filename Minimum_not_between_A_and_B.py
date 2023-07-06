n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in range(len(s)):
    if s[i]<a or s[i]>b:
        c.append(s[i])
    else:
        d.append(s[i])
if len(c)==0:
    print("-1")
else:
    print(min(c))
    