players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])#players의 0,1,2 index를 slice함.
print(players[:4])#처음부터 index(3)까지, florence까지 출력됨
print(players[2:])#3번째부터 마지막까지, michael부터 eli까지
print(players[-3:])#위와 같음, 뒤에서 3개 출력
print("\n")

print("Here are the first three players on my team:")
for player in players[:3]: 
	print(player.title())
print("\n")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # slice에 인덱스를 생략하면 전체 리스트반환. 이후에 수정하면 그건 따로따로 반영
print("my foods: ")
print(my_foods)
print("friends foods: ")
print(friend_foods)
