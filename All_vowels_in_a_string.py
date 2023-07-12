s=input()
l=['a','e','i','o','u']
a=[]
b=[]
for i in s:
    if i in l:
        a.append(i)
for i in a:
    if i not in b:
        b.append(i)
if len(b)==len(l):
    print("True")
else:
    print("False")