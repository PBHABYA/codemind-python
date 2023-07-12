s=input()
l=['a','e','i','o','u','A','E','I','O','U']
a=[]
for i in s:
    if i in l:
        a.append(i)
if len(a)>0:
    print(len(a))
else:
    print("0")
        