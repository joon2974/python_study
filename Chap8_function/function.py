def greet_user(username): #앞쪽이 fun이 아닌것만 빼면 코틀린, 다른언어와 비슷
	"""간단한 환영 인사를 표시합니다.""" #doc string: 함수기능 주석
	print("Hello, " + username.title() + "!")
	
greet_user('joon')#여기서 'joon'은 parameter
