n=int(input())
rev=0
t=n
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
if t==rev:
    print("True")
else:
    print("False")
