#Assignment 3
score = input("Enter Score: ")
try:
	fscore = float(score)
	if (fscore >= 0.9):
		print ('A')
	elif (fscore >= 0.8):
		print ('B')
	elif (fscore >= 0.7):
		print ('C')
	elif (fscore >= 0.6):
		print ('D')
	else:
		print ('F')
except:
	print ("Error: Please enter a score between 0.0 and 1.0")
