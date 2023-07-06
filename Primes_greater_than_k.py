n=int(input())
s=list(map(int,input().split()))
k=int(input())
d=[]
for i in s:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        d.append(i)
t=0
for i in range(len(d)):
    if d[i]>=k:
        t+=1
print(t)        
        
        

        
    