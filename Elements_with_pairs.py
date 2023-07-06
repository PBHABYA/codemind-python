n=int(input())
s=list(map(int,input().split()))
c=len(s)
if c%2==0:
    print(*s)
else:
    print(*s,end=" 0")