#user.py

from library import Base

assert hasattr(Base, 'foo'), 'you broke it, you idiot!'

class Derived(Base):
	def bar(self):
		return self.foo()	


