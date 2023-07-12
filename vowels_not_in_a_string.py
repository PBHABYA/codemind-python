s=input()
l=['a','e','i','o','u']
a=[]
b=[]
for i in s:
    if i in l:
        a.append(i)
for i in l:
    if i not in a:
        b.append(i)
if len(b)>0:
    print(*b)
else:
    print("0")
    