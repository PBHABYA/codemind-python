n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    c=c*2+int(i)
print(c)    