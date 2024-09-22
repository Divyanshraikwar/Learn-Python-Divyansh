n=int(input("Enter your number"))
for i in range(2,n,1):
    if(n%2==0):
        print("NOT PRIME")
        break
else:
     print("PRIME")