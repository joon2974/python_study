def show_magicians(magicians): 
	"""show magicians name"""
	for magician in magicians: 
		print(magician.title())
		
def make_great(magicians): 
	"""change magicians to great"""
	great_magicians = []
	
	while magicians: 
		magician = magicians.pop()
		great_magician = "Great " + magician
		great_magicians.append(great_magician)
		
	for great_magician in great_magicians: 
		magicians.append(great_magician)
		
magicians = ['alpha', 'beta', 'ceta']
show_magicians(magicians)

make_great(magicians[:])#사본전달. magicians는 바뀌지 않음.
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)
