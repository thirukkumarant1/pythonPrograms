a=input()
for i in range(0,len(a),2):
    if(a[i] in "123456789"):
        print(a[i+1]*int(a[i]))
    else:
        print(a[i]*int(a[i+1]))
        
    
    
    
