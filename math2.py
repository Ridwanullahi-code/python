import math
def trig():
	print("Welcome to degree finder app")

	number = (input("Enter thr degree value to find in sin,cos and tan "))

	search = int(input("Enter number to find it degree "))

	if number == "sin" and search == 15:
		result = (math.sin(45) * math.cos(30)) - (math.cos(45) * math.sin(30))
		print(result)
	elif number == "cos" and search == 15:
		result = (math.cos(45) * math.cos(30)) + (math.sin(45) * math.sin(30))
		print(result) 
	elif number == "tan" and search == 15:
		result = (math.tan(45) - math.tan(30))/ (1 - math.tan(45) * math.tan(30))
		print(result)


