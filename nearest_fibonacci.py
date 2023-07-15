fib=1000
n1,n2=0,1 
count=0

ram=[]
if fib==1:
    print(n1)
else:
    while count < fib+1:
        ram.append(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        
        count +=1 

bhavya=[]
z=int(input())
for i in ram:
    if i<=z:
        bhavya.append(i) 
    elif i>z:
        bhavya.append(i)
        break 


low=int(bhavya[-2])-z
high=z-(int(bhavya[-1]))
  

if low == high:
    print(bhavya[-2], bhavya[-1])
elif low > high:
    print(bhavya[-2]) 
elif low <high:
     print(bhavya[-1]) 
     
     
     