for i in range (1,6):
    for j in range (1,10):
        if (i==j) or (i==1 and j==9 ) or (i==2 and j==8) or (i==3 and j==7) or (i==4 and j==6): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
       
    print()
