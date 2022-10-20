from re import I


n=int(input("enter the number"))
a=0
b=1
i=0
while i<=n:
    print(i)
    a=b
    b=i
    i=a+b 