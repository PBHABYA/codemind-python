n=int(input())
s=list(map(int,input().split()))
c=[]
for i in s:
    if i not in c:
        c.append(i)
print(sum(c))