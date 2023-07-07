n=int(input())
s=list(map(int,input().split()))
c=0
d=[]
for i in s:
    i=str(i)
    a=i[::-1]
    d.append(a)
for i in range(n):
    if s[i]==int(d[i]):
        c+=1
print(c)        