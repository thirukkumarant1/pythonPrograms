a=input("enter the val")
count=1
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count=count+1
    else:
        print(a[i]+str(count),end="")
        count=1
print(a[i]+str(count),end="")        
        
    
