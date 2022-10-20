# for i in range (5,0,-1):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range (1,i+1):
#         print(k,end=" ")
#     print()

n=int(input("enter no:"))
i=n
while i>=1:
    k=0
    while k<=(n-i):
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    i=i-1
    print( )    