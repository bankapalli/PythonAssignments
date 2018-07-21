#Assignment 7
'''
Write a program for matrix multiplication
If Matrix1 is NxM and Matrix2 is MxL then Matrix1*Matrix2 is NxL, but Matrix2*Matrix1 is not valid
'''
matrix1 = [
			[3,2,5],
			[4,4,5]
		  ]
matrix2 = [
			[4,1],
			[3,2],
			[3,2]
		  ]

numberOfRowsInMatrix1 = len(matrix1)
numberOfColumnsInMatrix1 = len(matrix1[0])
numberOfRowsInMatrix2 = len(matrix2)
numberOfColumnsInMatrix2 = len(matrix2[0])

if(numberOfColumnsInMatrix1 != numberOfRowsInMatrix2):
	print ('Matrix multiplication is not possible for: Matrix1:',numberOfRowsInMatrix1, 'X', numberOfColumnsInMatrix1,'and Matrix2:',numberOfRowsInMatrix2, 'X', numberOfColumnsInMatrix2)
else:
	print ('Matrix multiplication is possiblefor: Matrix1:',numberOfRowsInMatrix1, 'X', numberOfColumnsInMatrix1,'and Matrix2:',numberOfRowsInMatrix2, 'X', numberOfColumnsInMatrix2)
	#Create an empty final list, the final list will be of size numberOfRowsInMatrix1 X numberOfColumnsInMatrix2
	finalList = list();
	x = 0
	while (x < numberOfRowsInMatrix1):
		tempList = list();
		y = 0
		while (y < numberOfColumnsInMatrix2):
			tempList.append(0)
			y = y+1
		finalList.append(tempList)
		x = x+1
	#The below loop is to iterate over each row in in matrix1
	for i in range(numberOfRowsInMatrix1):
	   #The below loop is to iterate over each column in in matrix2
	   for j in range(numberOfColumnsInMatrix2):
	       #The below loop is to iterate over each row in in matrix2
	       for k in range(numberOfRowsInMatrix2):
	           finalList[i][j] += matrix1[i][k] * matrix2[k][j]
	for r in finalList:
   		print(r)


'''
Notes: Below code to create the initial state of finalList did not work, because all the tempList's that we added to finalList are having same reference
Reference: https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
tempList = []
x = 0
while (x < numberOfColumnsInMatrix2):
	tempList.append(0)
	x = x+1
finalList = []
x = 0
while (x < numberOfRowsInMatrix1):
	finalList.append(tempList)
	x = x+1
'''