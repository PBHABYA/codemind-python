n=int(input())
s=list(map(int,input().split()))
a=int(input())
c=[]
for i in range(len(s)):
    if s[i]<=a:
        c.append(s[i])
    else:
       break
print(sum(c))        
    