n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if i%2==0:
        c+=i
    else:
        break
print(c)        