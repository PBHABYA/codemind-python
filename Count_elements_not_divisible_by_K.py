a,b=map(int,input().split())
s=list(map(int,input().split()))
c=0
for i in range(len(s)):
    if s[i]%b!=0:
        c+=1
print(c)        