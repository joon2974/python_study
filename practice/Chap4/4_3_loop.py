for value in range(1, 21): 
	print(value)
print("\n")

digits = [value for value in range(1, 1000001)]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")

odd_digits = [value for value in range(1, 21, 2)]
print(odd_digits)
for value in odd_digits: 
	print(value)
print("\n")

three_digits = [value for value in range(3, 31, 3)]
print(three_digits)
print("\n")

three_squares = [value**3 for value in range(1, 11)]
for value in three_squares: 
	print(value)
