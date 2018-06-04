def replaceBadWord(check):
	storge = ''
	for i in check:
		if (i == "<"):
			storge = storge + "&lt;"
		elif (i == ">"):
		
			storge = storge + "&gt;"
		else:
			storge = storge + i
			
	else:
		return storge
