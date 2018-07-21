#Assignment 5
'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
'''

largetNumberTillNow = None
smallestNumberTillNow = None

while True:
	userIput = input("Enter a number: ")
	if userIput == 'done':
		break
	try:
		userIput = int(userIput)

		if smallestNumberTillNow is None:
			smallestNumberTillNow = userIput
		elif smallestNumberTillNow > userIput:
			smallestNumberTillNow = userIput 

		if largetNumberTillNow is None:
			largetNumberTillNow = userIput
		elif largetNumberTillNow < userIput:
			largetNumberTillNow = userIput 

	except:
		print('Invalid input')
print('Maximum is',largetNumberTillNow)
print('Minimum is',smallestNumberTillNow)