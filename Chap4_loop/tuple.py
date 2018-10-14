#바뀌지 않는 리스트를 '튜플'이라고 함.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 / 튜플의 값을 직접 변경할 수는 없다.
print("\n")

for dimension in dimensions: 
	print(dimension)
# list처럼 튜플도 for문 사용 가능
print("\n")

dimensions = (400, 40)#값 하나를 변경할 수는 없지만 전체를 덮어서 수정할수는 있음!!
print("Modified dimensions: ")
for dimension in dimensions: 
	print(dimension)
#옆의 세로줄은 pep8에 의한 글자수 제한을 표현한 것임
