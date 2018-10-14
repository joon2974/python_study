lists = ['a' ,'b', 'c', 'd', 'e', 'f']
print(lists[:3])
print(lists[-3:])
print(lists[1:4])
print("\n")

pizzas = ['불고기', '치즈', '콤비네이션']
friend_pizzas = pizzas[:]#이렇게 복사하면 서로 별개의 list가 됨
pizzas.append('베이컨')
friend_pizzas.append('모짜렐라')
print("내가 좋아하는 피자는: ")
for pizza in pizzas: 
	print(pizza)
print("\n")
print("친구가 좋아하는 피자는: ")
for pizza in friend_pizzas: 
	print(pizza)
