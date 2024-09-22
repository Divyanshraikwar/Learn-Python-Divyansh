n=int(input("Enter the number:"))
a=0
b=1
s=0
for i in range(1,n+1,1):
    print(a,end=" ")
    s=a+b
    b=a
    a=s