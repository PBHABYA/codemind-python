n=int(input())
s=list(map(int,input().split()))
c=0
avg=sum(s)//len(s)
for i in range(n):
    if s[i]>=avg:
        c+=1
print(c)        