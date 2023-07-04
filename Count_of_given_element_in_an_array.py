n=int(input())
s=list(map(int,input().split()))
m=int(input())
c=0
for i in s:
    if(i == m):
        c+=1
print(c)