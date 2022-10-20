i=1
count=0
user=int(input("enter the number"))
while i<=user:
    if user%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime")
else:
    print("not a prime")