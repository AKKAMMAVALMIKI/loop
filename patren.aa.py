# s=input("enter the string:")
# length=len(s)
# for i in range (length):
#     for j in range (i+1):
#         print(s[j],end=" ")
#     print()




n=input("enter word:")
a=len(n)
i=0
while i<a:
    j=0
    while j<=i:
        print(n[j],end=" ")
        j=j+1
    i=i+1
    print( )    