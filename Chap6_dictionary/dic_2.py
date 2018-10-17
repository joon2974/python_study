alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': 5}
print("Original x-position: " + str(alien_0['x_position']))

#외계인을 오른쪽으로 이동
#현재 속도 기준, 얼마나 빨리 움직이는지 판단
if alien_0['speed'] == 'slow': 
	x_increment = 1
elif alien_0['speed'] == 'medium': 
	x_increment = 2
else: 
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print("\n")

print(alien_0)
del alien_0['points']#딕셔너리의 키-값 제거, 복구할 수 없음!!
print(alien_0)
speed = alien_0.pop('speed')#pop도 사용 가능!!
print(speed)
print(alien_0)
