def make_album(name, album_title, num_songs=''): 
	"""앨범과 뮤지션에 대한 정보 반환"""
	music_album = {'name': name, 'album_title': album_title}
	if num_songs: 
		music_album['num_songs'] = num_songs
	return music_album

while True: 
	print("\nPlease enter name and title.")
	print("If you want to stop. press 'q' anytime.\n")
	
	n = input("Musicians name: ")
	if n == 'q': 
		break
	t = input("Title: ")
	if t == 'q': 
		break
	s = input("Number of songs: ")
	if s == 'q': 
		break
	
	if s: 
		result = make_album(n, t, s)
	else: 
		result = make_album(n, t)
		
	print("\n")
	for key, value in result.items(): 
		print(key + ": " + str(value))

