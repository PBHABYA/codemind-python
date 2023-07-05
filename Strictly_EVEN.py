n=int(input())
s=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if s[i]%2==0:
        c+=1
    if i%2==0 and s[i]%2==0:
        d+=1
if c==d:
    print("True")
else:
    print("False")
        