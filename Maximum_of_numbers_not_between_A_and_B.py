n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(n):
    if s[i]<a or s[i]>b:
        l.append(s[i])
if len(l)==0:
    print("-1")
else:
    print(max(l))