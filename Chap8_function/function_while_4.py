def get_formatted_name(first_name, last_name): 
	"""읽기 쉬운 전체 이름 반환"""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	
while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q': 
		break
		
	l_name = input("Last name: ")
	if l_name == 'q': 
		break
		
	print("\nHello, " + get_formatted_name(f_name, l_name) + "!")
