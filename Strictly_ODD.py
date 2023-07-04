n=int(input())
s=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if i%2==1:
        c+=1
    if i%2==1 and s[i]%2==1:
        d+=1
if c==d:
    print("True")
else:
    print("False")