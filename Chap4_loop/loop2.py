for value in range(1,5): #끝 숫자는 포함하지 않음
	print(value)#1~4까지만 출력
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))#2씩 증가시킴
print(even_numbers)
print("\n")

squares = []
for value in range(1,11): 
	square = value**2
	squares.append(square) #squares.append(value**2) 같은코드임
print(squares)
print("\n")

squares1 = [value**2 for value in range(1,11)]#리스트 내포로 표현
print(squares1)
print("\n")

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")
