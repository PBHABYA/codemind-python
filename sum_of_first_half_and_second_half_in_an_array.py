n=int(input())
s=list(map(int,input().split()))
c=len(s)
d=c//2
a=s[0:d]
b=s[d:]
print(sum(a))
print(sum(b))