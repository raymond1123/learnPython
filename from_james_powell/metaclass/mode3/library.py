# library.py

class BaseMeta(type):
	def __new__(cls, name, bases, body):
		#print('BaseMeta.__new__', cls, name, bases, body)
		if name is 'Derived' and not 'bar' in body:
			raise TypeError('bad user class')
		return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
	def foo(self):
		return 'foo'


