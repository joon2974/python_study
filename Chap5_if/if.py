cars = ['audi', 'bmw', 'kia', 'hyundai']
for car in cars: 
	if car == 'bmw': 
		print(car.upper())
	else: 
		print(car.title())
print("\n")
car = 'Audi'
print(car == 'audi')#대소문자를 구별!
print(car.lower() == 'audi')#일시적으로 소문자로 바꿈!
print(car)
print("\n")

age_0 = 22
age_1 = 18
if age_0 == 22 and age_1 == 18: 
	print("True")
#and와 or로 다중 조건문 가능
print("\n")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("Are there mushrooms in requested toppings??")
print('mushrooms' in requested_toppings)#리스트 내에 존재하는지 in 으로확인
print("\n")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users: 
	print(user.title() + ", you can post a reponse if you wish.")
#not으로 리스트 안에 없는지 확인 가능
