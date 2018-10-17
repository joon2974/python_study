age = 17
if age >= 18: 
	print("You are old enough to vote!")
else: 
	print("Sotty, you are too young to vote.")

age = 12
if age < 4: 
	print("Your admission cost is $0.")
elif age < 18: #else if 가 아니라 elif로 사용함!!
	print("Your admission cost is $5.")
else: 
	print("Your admission cost is $10.")
#마지막에 else보다 elif를 사용하면 더 정확한 조건에서 실행이 가능!
