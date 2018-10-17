#확인해야 하는 사용자 리스트
#확인된 사용자를 저장할 빈 리스트로 시작
unconfirmed_users = ['alice', 'brian', 'Candace']
confirmed_users = []

#확인되지 않은 사용자가 없을때까지 확인
#확인된 사용자는 확인된 리스트로 옮김
while unconfirmed_users: 
	current_user = unconfirmed_users.pop()
	
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

#확인된 사용자 출력
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: 
	print(confirmed_user.title())
print("\n")
	
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets: #cat을 전부 제거
	pets.remove('cat')
	
print(pets)
