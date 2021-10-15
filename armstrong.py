'''n=int(input())
b=n
sum1=0
while(n>0):
    rem=n%10
    sum1=sum1+rem**3
    n=n//10
print(sum1)
if(b==sum1):
    print(f" {sum1}  is armstrong no")
else:
    print(f"{sum1} is not armstrong no")'''
    
n=int(input())
sum1=0
for i in range(1,n):
    if(n%i==0):
        print(i)
        sum1=sum1+i
if(sum1==n):
    print(f"{sum1} is perfect")
else:
    print(f"{sum1} is not perfect")
    
