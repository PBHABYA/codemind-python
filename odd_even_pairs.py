n=int(input())
s=list(map(int,input().split()))
b=[]
a=[]
for i in s:
    if i%2==0:
        b.append(i)
    else:
        a.append(i)
i=0
j=0 
while i<len(a) or j<len(b):
    if i<len(a):
        print(a[i],end=" ")
        i+=1
    if j<len(b):
        print(b[j],end=" ")
        j+=1
if n%2==1:
    print("0")
        
        
        