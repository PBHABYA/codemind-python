n=int(input())
a=0
b=1
c=a+b
if n==0:
    print("True")
while c<n:
    c=a+b
    a=b
    b=c
if c==n:
    print("True")
else:
    print("False")
    