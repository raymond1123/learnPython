# dec.py

from time import time

def timer(func):
	def f(*args, **kwargs):
		before = time()
		rv = func(*args,)
		after = time()
		print('elapsed', after - before)
		return rv
	return f

# @timer <=> add = timer(add)
#@timer
#def add(x,y=10):
#	return x + y
##add = timer(add)


# @timer <=> sub = timer(sub)
#@timer
#def sub(x, y=10):
#	return x - y
##sub = timer(sub)
	


#print('add(10)', add(10))
#print('add(20, 30)', add(20, 30))
#print('add("a", "b")', add("a", "b"))
#print('sub(10)', add(10))
#print('sub(20, 30)', add(20, 30))
#print('sub("a", "b")', add("a", "b"))


#print(type(timer(add)))


def ntimes(n):
	def inner(f):
		def wrapper(*args, **kwargs):
			for _ in range(n):
				print('running {.__name__}'.format(f))
				rv = f(*args, **kwargs)
			return rv
		return wrapper

	return inner


@ntimes(2)
def add(x, y=10):
	return x + y

@ntimes(3)
def sub(x, y=10):
	return x - y


print('add(10)', add(10))
print('sub(10)', sub(10))



