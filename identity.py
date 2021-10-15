para="the lion is the king of the jungle th"
list1=list(para.strip())
list2=list(para.split())
b=input()
for i in list2:
    if(i.startswith(b)):
      print(i)
