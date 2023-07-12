s=input().split()
l=['a','e','i','o','u']
c=[]
for i in s:
    d=0
    for j in i:
        if j in l:
            d+=1
    c.append(d)
print(c.count(max(c)))       