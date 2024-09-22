even=odd=1
for i in range(1,21,1):
    if(i%2==0):
        even*=i
    else:
        odd*=i
print("even=",even)
print("odd=",odd)