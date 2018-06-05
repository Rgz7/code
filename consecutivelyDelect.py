#de
import re 

def repeatToOne(sample):
	storge = ''
	repeatword = ''
	repeat = 1
	beforeword = ''
	sampleLen = len(sample)
	print("total",sampleLen)
	for i in sample: 
		sampleLen -= 1 
		if ((repeat == 1) and (i != beforeword)):
			storge = storge + i
			beforeword = i 
		elif (((repeat >= 1) and (i != beforeword)) or ((sampleLen == 0) and (repeat > 1))):			
			storge = storge.replace(repeat * beforeword,beforeword)
			print('storge',storge)
			if (sampleLen != 0):
				storge = storge + i 
			repeat = 1
			beforeword = i 			
		else:
			repeat = repeat + 1 
			storge = storge + i 
	return storge 
	
test = "asdfasdddassassfsfffffff"
print(repeatToOne(test))
