current_number = 0
while current_number < 10: 
	current_number += 1
	if current_number % 2 == 0: 
		continue #루프의 시작으로! 밑의 코드는 무시
	
	print(current_number)
#1 3 5 7 9 를 출력함
