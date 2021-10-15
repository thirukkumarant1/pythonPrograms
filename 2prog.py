words=input("enter the words").split(",")
a=input("enter the aAlpha").split(",")
print(a)
s=""
s=s.join(a)
print(s)


for i in range(0,len(words),1):
    if(s in  words[i]):
        print(words[i])
        

