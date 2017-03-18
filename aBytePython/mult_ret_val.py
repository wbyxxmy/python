import math

def mov(x, y, step, angle=0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx, ny
	