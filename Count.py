n=int(input())
s=list(map(int,input().split()))
c=0
d=0
for i in s:
    if i%2!=0:
        d+=1
    else:
        c+=1
print(c,d)
