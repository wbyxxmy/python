ab = {
	'zhangsan' : 'zhangsan@qq.com',
	'lisi' : 'lisi@chinaredstar.com',
	'wangwu' : 'wangwu@163.com',
	'zhaoliu' : 'zhaoliu.123.com'	
	}
	
print("zhangsan's address :", ab['zhangsan'])

del ab['zhangsan']
print("There are {0} items in ab".format(len(ab)))
for name,address in ab.items():
	print("{0}'s address is :{1}".format(name,address))
ab['gougou'] = 'gougou@qwe.com'
if 'gougou' in ab:
	print("gougou's address is", ab['gougou'])
