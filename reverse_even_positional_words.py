n=input()
n=list(n.split())
c=[]
for i in range(len(n)):
    if i%2==0:
        i=n[i]
        a=list(i)
        a.reverse()
        x=''.join(a)
        c.append(x)
    else:
        c.append(n[i])
print(*c)        