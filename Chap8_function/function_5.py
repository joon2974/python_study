def make_pizza(size, *toppings): 
	# 매개변수가 여러개 일때는 *가 맨 뒤에 있어야 함
	# *뜻 : 빈 튜플을 만들고 받는 값을 모두 이 튜플에 저장
	"""만들려고 하는 피자를 요약"""
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings: 
		print("- " + topping)
	
make_pizza(16, 'pepperoini')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
