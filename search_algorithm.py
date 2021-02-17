loop = True
while loop == True:

	num1 = int(input("Enter your first number : "))
	operator= input("Enter operator: ")
	num2 = int(input("Enter your second number : "))

	if operator == "+":
		print(num1 + num2)

	elif operator == "-":
		print(num1 - num2)

	elif operator == "*":
		print(num1 * num2)

	elif operator == "%":
		print(num1 % num2)

	elif operator == "/":
		print(num1 / num2)

	else:
		loop = False


