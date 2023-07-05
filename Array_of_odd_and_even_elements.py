n=int(input())
s=list(map(int,input().split()))
l=[]
h=[]
for i in range(len(s)):
    if s[i]%2==1:
        l.append(s[i])
    else:
        h.append(s[i])
print(*(l+h))        
        
    
        
        