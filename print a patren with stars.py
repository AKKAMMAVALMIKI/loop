r=5
c=5
i=1
while i<=r:
    j=1
    while j<=c:
        if (i==1 and j==3) or (i==2 and j==2) or (i==2 and j==4) or (i==3 and j==1) or (i==3 and j==5) or (i==4 and j==1)or  (i==4 and j==2) or (i==4 and j==3)or (i==4 and j==4) or (i==4 and j==5) or (i==5 and j==1) or (i==5 and j==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()




# for i in range (1,6):
    # for j in range (1,6):
    #     if (i==1 and j==3) or (i==2 and j==2) or (i==2 and j==4) or (i==3 and j==1) or (i==3 and j==5) or (i==4 and j==1)or  (i==4 and j==2) or (i==4 and j==3)or (i==4 and j==4) or (i==4 and j==5) or (i==5 and j==1) or (i==5 and j==5):
    #         print("*",end=" ")
    #     else:
    #         print(" ",end=" ")
       
    # print()





# i=1
# while i<=3:
#     j=1
#     p=1
#     while j<=i:
#         print(i*j,end="")
        
#         j=j+1
#     print()
#     i=i+1