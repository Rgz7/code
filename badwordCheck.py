def replaceBadWord(check):
	storge = ''
	for i in check:
		if (i == "<"):
			storge = storge + "&lt;"
		elif (i == ">"):
		
			storge = storge + "&gt;"
		# you can add more elif condition here.
		else:
			storge = storge + i
			
	else:
		return storge
