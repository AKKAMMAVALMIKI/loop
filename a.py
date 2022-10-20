# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if (i==1 and j==1) or (i==2 and j==1)or (i==2 and j==2) or (i==3 and j==1) or (i==3 and j==2) or (i==3 and j==3) or (i==4 and j==1) or (i==4 and j==2) or (i==5 and j==1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j=j+1
#     i=i+1
#     print()  






n= int(input("enter the number"))
i=1
while i<=n:
    print("*"*i)
    i=i+1
i=n-1
while i>=1:
    print("*"*i) 
    i=i-1   