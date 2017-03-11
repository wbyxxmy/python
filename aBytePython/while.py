# !/user/bin/python
# Filename while.py

number = 23
running = True

while running:
	guess = int(input("Enter an integer:"))
	if guess == number:
		print("You are right!!!")
		running = False
	elif guess > number:
		print("too large!!!")
	else:
		print("too small!!!")
else:
	print("while over.")
print("done")