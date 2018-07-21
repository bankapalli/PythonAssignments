#Assignment 8
'''
Write a program to print all prime numbers between 1 to 50
Prime Number Definition: A number is a prime number if it has only 2 factors
'''
i = 1
while (i <= 50):
	j = 1
	count = 0
	while (j <= 50):
		if (i%j == 0):
			count = count + 1;
		j = j+1
	if (count == 2):
		print (i)
	i=i+1