


def f(a, b, *arg):
	print (a)
	print (b)

	print (type(arg))
	print (arg)


#f(1,2,3,4,5)
#f(1,2,[1,2,3], [4,5,6])


def ff(a, b, **kw):
	print (a)
	print (b)

	print (type(kw))
	print (kw)

#ff(1,2, name='abc', age=12)

