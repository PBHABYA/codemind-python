n=int(input())
s=list(map(int,input().split()))
d=[]
for i in s:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
       d.append(i)
avg=(sum(d)/len(d))
print('%.2f'%avg)
       
    