class simpleinterest:
	def __init__(self,principal,rate,time):
		self.principal=principal
		self.rate=rate
		self.time=time
def show(self):
	print("principal=",self.p)
	print("rate=",self.rate)
	print("time=",self.time)
def sical(self):
	return self.p*self.rate*self.time/100
i1= simpleinterest(1000,10,2)
i1.show()
print("simple interst=",i1.sical())