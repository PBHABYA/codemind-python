n=int(input())
s=list(map(int,input().split()))
c=[]
for i in s:
    i=str(i)
    i=list(i)
    i.reverse()
    i=''.join(i)
    i=int(i)
    c.append(i)
print(*c)