current_number = 1
while current_number <= 5: 
	print(current_number)
	current_number += 1
	
prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != 'quit': #여기서 비교할 값이 필요하므로 message를 먼저 선언.
	message = input(prompt)
	if message != 'quit':
		print(message)

