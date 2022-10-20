n=int(input("enter the number of terms"))
i=1
odd=0
even=0
while i<=n:
    if i%2==0:
        even=even+i*i
    else:
        odd=odd+i*i
    i=i+1
    print(even-odd)

