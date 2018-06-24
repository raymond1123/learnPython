#library.py

'''
class Base:
	def foo(self):
		return 'foo'

old_bc = __build_class__

def my_bc(*a, **kw):
	print ('my build class->', a, kw)
	return old_bc(*a, **kw)

import builtins
builtins.__build_class__ = my_bc

'''

class BaseMeta(type):
	def __new__(cls, name, bases, body):
		#print('BaseMeta.__new__', cls, name, bases, body)
		if not 'bar' in body:
			raise TypeError("bad user class")
		return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
	def foo(self):
		return self.bar()

	def bar():
		return 'yes'

	# seems __init_subclass__ only for python 3.6
	# let's just ignore this method
	def __init_subclass__(cls, *a, **kw):
		print('init_subclass', a, kw)
		return super().__init_subclass__(cls, *a, **kw)
		
