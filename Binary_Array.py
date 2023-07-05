n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if i==1 or i==0:
        c=1
    else:
        c=0
if c==1:
    print("True")
else:
    print("False")