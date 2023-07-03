n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(len(s)):
    if i%2==1:
        c+=s[i]
print(c)        