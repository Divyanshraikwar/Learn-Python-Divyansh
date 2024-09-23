sum=0
n=int(input("enter n"))
if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "is not a prime number")
		break
	else:
		print(n, "is a prime number")
while(n!=0):
    r=n%10
    sum+=r
    n=n//10
print(sum)
# If the number is less than 1, its also not a prime number.
else:
	print(n, "is not a prime number")
