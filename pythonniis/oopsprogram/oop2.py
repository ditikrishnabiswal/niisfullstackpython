# write a program to display 2 student name ,rollno,mark
class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r 
		self.mark=m 
	def show (self):
		print("my name=",self.name)
		print("my roll=",self.roll)
s1=student("muna",1,90.50)
s2=student("kuna",2,80.50)
s1.show()
s2.show()