cars = ['bmw', 'audi', 'kia', 'hyundai']
cars.sort()#리스트를 영구적으로 소팅(알파벳순)
print(cars)
cars.sort(reverse = True)#알파벳 역순 정렬
print(cars)
print("\n")

print("original list")
print(cars)
print("sorted list")
print(sorted(cars))#임시적으로 정렬
print("original list")
print(cars)
print("\n")

cars = ['bmw', 'audi', 'kia', 'hyundai']
print(cars)
cars.reverse()#알파벳 관계없이 순서만 반대로
print(cars)
print("\n")

print(len(cars))#리스트 길이
