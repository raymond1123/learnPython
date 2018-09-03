# user.py
from library import Base

# if dev of lib delete func foo, then the bar method crash
# any idea that will prevent this just before run time?
# just a assert and hasattr will do
# 29'

assert hasattr(Base, 'foo'), "you broke it! you fool!"

class Derived(Base):
	def bar(self):
		return self.foo()

