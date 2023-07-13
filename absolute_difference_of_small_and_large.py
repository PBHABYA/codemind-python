n=input().split()
a=[]
for i in n:
    x=ord(max(i))-ord(min(i))
    a.append(x)
print(*a)   