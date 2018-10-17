prompt = "Please input your age: "
while True: 
	age = input(prompt)
	
	if age == 'quit': 
		break
	else: 
		age = int(age)
		if age < 3: 
			print("You're free!")
		elif age >= 3 and age <=12: 
			print("You have to pay 10 dollers.")
		elif age >= 13: 
			print("You have to pay 15 dollers.")
