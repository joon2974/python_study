aliens = []#alien 딕셔너리들을 저장할 리스트

for alien_number in range(30): 
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	
#처음 세마리만 설정을 변경
for alien in aliens[0:3]: 
	if alien['color'] == 'green': 
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[:5]: #처음부터 5개까지만 출력
	print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))
