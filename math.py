import math 
print("Welcome to degree finder app")

number = (input("Enter thr degree value to find in sin,cosine and tangent "))

search = int(input("Enter number to find it degree"))

if number == "sin":

	degree = math.sin(search)

	print(degree)

elif number == "cos":

	degree = math.cos(search)
	print(degree)
	
elif number == "tangent":
	degree = math.tangent(search)
	print(degree)