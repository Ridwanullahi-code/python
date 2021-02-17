# conditional for looping
try_again = 0
print("Welcome to the Temperature Converter. Type C for Celsius, F for Fahreinheit and K for Kelvin ") 
while try_again <= 10:
	# Function
	def again():
		# Letting the user choose the temperature and convert it to another else
		user_temperature = str(input("User Enter C | F| K | ")).upper()
		converter_Temperature = str(input("The temperature you want to convert to | C | F | K | ")).upper()
		degree = int(input("Enter the degree: "))
	# if the user's initial Temperature (C , F or K) convert it to what the user wants to convert to (C, F, or K) and give him the equation
		# conversion of celsius to fahrenheit
		if user_temperature == "C" and converter_Temperature == "F":		
			result = (degree * 9/5) + 32
			print(f"{result}F \nThe equation: ({degree} * 9/5) + 32 = {result}")
		# conversion of celsius to kelvin
		elif user_temperature == "C" and converter_Temperature == "k":
			result = 273.15 + degree
			print(f"{result}K \nThe equation: 273.15 + {degree} = {result}")
		# conversion of fahrenheit to celsius
		elif user_temperature == "F" and converter_Temperature == "C":
			result = (degree - 32) * 5/9
			print(f"{result}C \nThe equation: (degree - 32) * 5/9 = {result}")
		# conversion of fahrenheit to kelvin
		elif user_temperature == "F" and converter_Temperature == "K":
			result = (degree - 32) * 5/9 + 273.15
			print(f"{result}C \nThe equation: (degree - 32) * 5/9 + 273.15 = {result}")

		elif user_temperature == "K" and converter_Temperature == "C":
			result = degree - 273.15
			print(f"{result}C \n The equation: degree - 273 = {result}")

		elif user_temperature == "K" and converter_Temperature == "F":
			result = (degree - 273.15) * 9/5 + 32
			print(f"{result}F \nThe equation: (degree - 273.15)9/5 + 32 = {result}")
	
	try_again += 1

	temp = print(again())
	print(temp)






















