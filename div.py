a=int(input())
b=int(input())
c=int(input())
d=a+b
e=b+c
f=c+a
g=a&b
h=b&c
i=c&a
if((d>e) and (d>f) and (d>g) and (d>h) and (d>i)):
    print(f"{d} is greater")
elif((e>f) and (e>g) and (e>h) and (e>i)):
     print(f"{e} is greater")
elif((f>g)  and (f>h) and (f>i)):
    print(f"{f} is greater")
elif((g>h) and (g>i)):
    print(f"{g} is greater")
elif((h>i)):
    print(f"{h} is greater")
else:
    print(f"{i} is greater")
List =[a,b,c,d,e,f,g,h,i]
List.sort()
print(List)
List.reverse()
print(List)
