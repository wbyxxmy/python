def my_abs(x):
	if not isinstance(x,(float,int)):
		raise TypeError('Bad Request!!!')
	if x>=0:
		return x;
	else:
		return -x;
	