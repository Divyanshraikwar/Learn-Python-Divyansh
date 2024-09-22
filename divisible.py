a=int(input("Enter a value of a"))
if(a%3==0 and a%7==0):
    print(a,"is divisible by both 3 and 7")
elif(a%3==0):
    print(a,"is divisible by 3")
elif(a%7==0):
    print(a,"is divisible by7")
else:
    print("not divisible")
