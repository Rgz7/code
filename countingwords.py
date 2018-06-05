#counting charactor
import re 

def countingwords(sample):
	remember = []
	for i in sample:
		if (i not in remember):
			getTarget = re.findall(i,sample)
			print(i,len(getTarget))
			remember.append(i)

test = "abcdccaaddbkfdka"
countingwords(test)
