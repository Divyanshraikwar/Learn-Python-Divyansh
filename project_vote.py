age=int(input("Enter your age"))
if(age<=17):
    print(("YOU ARE NOT ELIGIBLE"))
elif(age>=18):
    print("YOU ARE ELIGIBLE FOR VOTING")
    print('''press 1 for "BJP" 
press 2 for "BSP"
press 3 for "cpi"
press 4 for "ncp" ''')
    choice=int(input("Enter your choice"))
    if(choice==1):
        print("congrats,you succefully vote BJP")
    elif(choice==2):
        print("congrats , you vote BSP")
    elif(choice==3):
        print("congrats, you CPI")
    elif(choice==4):
        print("congrats, you vote NCP")
        print("Thanks for voting")
    
    
    