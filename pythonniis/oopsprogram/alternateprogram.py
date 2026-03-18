class student:
	def __init__(self,name):
		self.__name=name
@property
def name(self):
	return self.__Name 
@name.setter 
def name(self,value):
	self.__name=value
s=student("muna")
print(s.name)
s.name="Rahul"
print(s.name)
	