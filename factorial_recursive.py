def factorial(value):
	if (value==1) or (value==0):
		return 1
	else:
		return value*factorial(value-1)
n=int(input("Enter the integer value for factorial:"))
if n<0:
	print("Enter valid number")
else:
	factorial_value=factorial(n)
	print("The factorail for the number",n,"is",factorial_value)
