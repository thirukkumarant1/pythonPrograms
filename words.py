a=input("enter the elements")
vcount=0
scount=0
ccount=0
for i in range(len(a)):
    if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
        vcount+=1
    elif(a[i]=="&" or a[i]=="#" or a[i]=="@"):
        scount+=1
    else:
        ccount+=1
print(vcount)
print(scount)
print(ccount)
    
