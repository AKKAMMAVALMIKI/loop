from audioop import avg


i=1
sum=0
while i<=10:
    user=int(input("enter the number"))
    sum=sum+user
    i=i+1
avg=sum/10
print(avg)