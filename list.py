n=int(input())
a=[]
evenlist=[]
oddlist=[]
for i in range(n):
    no=int(input())
    a.append(no)
print(a)
for i in range(len(a)):
    if(a[i]%2==0):
        evenlist.append(a[i])
        
    else:
        oddlist.append(a[i])
        
print(evenlist)
print(oddlist)
    
    
