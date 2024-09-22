print('''press "A" for addition
press "S" for subtraction
press "D" for division
press "M" for multiplication''')
opera=input("SELECT OPERATION")
if(opera=="A"):
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))
    result=num1+num2
    print(result)
elif(opera=="S"):
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))
    if(num1>num2):
        result=num1-num2
        print(result)
    else:
        (num2>num1)
        result=num1-num2
        print(result)
elif(opera=="D"):
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        result=num1//num2
        print(result)
elif(opera=="M"):
        num1=int(input("Enter first number"))
        num2=int(input("Enter second number"))
        result=num1*num2
        print(result)
    
