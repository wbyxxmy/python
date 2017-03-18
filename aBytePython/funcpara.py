#!/usr/bin/env python
# -*- coding: utf-8 -*-

def area_of_circle(r):
	pi = 3.14
	return pi*r**2
	
def addup(start, end, func):
	total = 0
	for i in range(start,end):
		total += func(i)
	return total

def func1(x):
	return x
	
def func2(x):
	return x**2 + 1
	
print(area_of_circle(10))
print(addup(1,5,func1))
print(addup(1,5,func2))