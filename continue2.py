n1=int(input("Enter the breaking point"))
n2=int(input("Enter the breaking point"))
n3=int(input("Enter the breaking point"))
for i in range(51):
    if(i==n1 or i==n2 or i==n3):
        continue
    print(i)