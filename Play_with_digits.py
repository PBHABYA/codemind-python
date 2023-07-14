n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    i=str(i)
    for j in i:
        j=int(j)
        c+=j
print(c)
        