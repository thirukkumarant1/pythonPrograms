#bucket="H,F,B,A,C,L,K,G,V,C,B,I,U,K,F".split(",")
#word="BLACKBUCK"
bucket = input("enter a string").split(",")
no=int(input())
for k in range(no):
    word=input()
print(word)    
    
    

count=0
for i in range(len(word)):
    if(word[i] in bucket):
        count+=1
        bucket.remove(word[i])
if(count == len(word)):
    print("yes")
else:
    print("no")
        
        
        
            
