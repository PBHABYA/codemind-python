n=int(input())
sum=0
i=0
while n!=0:
    j=n%10
    sum=sum+j*(8**i)
    n=n//10
    i+=1
print('{0:b}'.format(sum))    
    