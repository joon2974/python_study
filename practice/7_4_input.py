prompt = "Please enter topping you want."
prompt += "\n(If you want to finish, enter 'quit'): "

while True: 
	message = input(prompt)
	if message == 'quit': 
		break
	else: 
		print("I will add " + message + " on your pizza.\n")

