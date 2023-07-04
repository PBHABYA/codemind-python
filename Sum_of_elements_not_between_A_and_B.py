n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
l=0
for i in range(n):
    if s[i]<a or s[i]>b:
        l+=s[i]
print(l)        
        
    