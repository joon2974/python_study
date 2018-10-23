def make_shirt(size='L', message='I love Python'): 
	"""셔츠 사이즈와 메세지 출력"""
	print("Your shirt's size is: " + size + " and message is: " + 
		message.title())
		
make_shirt('L', 'Lucky')
make_shirt(size = 'M', message = 'monster')
make_shirt()
make_shirt('XL', 'hamburger')
