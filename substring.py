def solve(n,k,str1,str2):
    for i in str1:
        for j in str2:
            if (j in i):
               print("yes")
            else:
                print("no")
n=int(input())
k=int(input())
str1=input()
str2=input()

solve(n,k,str1,str2)
