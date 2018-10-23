def make_album(name, album_title, num_songs=''): 
	"""앨범과 뮤지션에 대한 정보 반환"""
	music_album = {'name': name, 'album_title': album_title}
	if num_songs: 
		music_album['num_songs'] = num_songs
	return music_album
	
m = make_album('epic high', 'flower', 11)
for key, value in m.items():
	print(key + ": " + str(value)) 
m = make_album('10cm', 'help')
print(m)
m = make_album('list', 'la campanela', 5)
print(m)
#print(make_album('sd', 'sd'))이렇게 호출하면 이상한 결과가 나옴.
