# n=int(input("ente the number of rows:"))
# k=ord("A")
# for i in range (n):
#     for j in range (i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()



n=int(input("entr the number"))
i=1
k=ord("A")
while i<=n:
    j=1
    # k=ord("A")
    while j<=i:
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    i=i+1
    print()
