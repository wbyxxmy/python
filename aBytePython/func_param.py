# !/usr/bin/python
# Filename: func_param.py

def printMax(a,b):
	if a > b:
		print(a, 'is maxnum')
	elif a == b:
		print(a, 'is equal to', b)
	else:
		print(b, 'is maxnum')
	
printMax(3,4)

x = 9
y = 3

printMax(x, y)