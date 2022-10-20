# n=int(input("enter the number"))
# for i in range (1,n+1):
#     for j in range (1,n-i,+1):
#         print(" ",end=" ")
#     for j in range (i,0,-1):
#         print(j,end=" ")
#     for j in range (2,i+1,1):
#         print(j,end=" ")
#     print()

n=int(input("enter no:"))
i=1
while i<=n:
    k=0
    while k<=(n-i):
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=1:
        print(j,end=" ")
        j=j-1
    m=2
    while m<=i:
        print(m,end=" ")
        m=m+1    
    i=i+1
    print( )    



