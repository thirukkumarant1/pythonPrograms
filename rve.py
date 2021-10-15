n=int(input())
reverse=0
sum1=0
while(n>0):
    rem=n%10
    '''reverse=(reverse*10)+rem'''
    sum1=sum1+(n%10)
    n=n//10
    print(rem,end="+")   

    '''print(reverse)'''
