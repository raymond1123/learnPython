# library.py

class Base:
	def foo(self):
		return 'foo'

old_bc = __build_class__

""" 
def my_bc(*a, **kw):
	print('my build_class ->', a, kw)
	return old_bc(*a, **kw)
""" 


# 40'
def my_bc(func, name, base=None, **kw):
	if base is Base:
		print('check if method bar defined')
	if base is not None:
		return old_bc(func, name, base, **kw)
		
	return old_bc(func, name, **kw)


import builtins
builtins.__build_class__ = my_bc


