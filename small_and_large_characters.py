s=input().split()
c=[]
for i in s:
    a=ord(max(i))
    b=ord(min(i))
    c.append(chr(b))
    c.append(chr(a))
print(*c)    