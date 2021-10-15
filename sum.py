n=int(input())
s=0
for i in range(1,n+1):
    s=s+i
    if(i!=n):
        print(i,end="+")
    else:
        print(i,"=",s)
