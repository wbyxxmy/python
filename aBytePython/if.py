#! /usr/bin/python
# Filename: if.py

number = 23
guess = int(input('Enter an integer: '))

if guess == number:
	print('Congratulations, you guessed it.') # New block starts here
	print('(but you do not win any prizes!)') # New block ends here 
elif guess < number:
	print('No, it is a little lower than that')
else:
	print('No, it is a little lower than that')
print('Done')