n=int(input())
lst=[]
for k in range(0,n):
    no=int(input("enter the elemets"))
    lst.append(no)
temp=0    
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[j]<lst[i]:
            temp = lst[i]    
            lst[i]=lst[j]    
            lst[j]=temp
print(lst)            
