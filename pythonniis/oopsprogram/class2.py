class person:
	def dispaly_person(self):
		print("this is a person")
class student(person):
	def dispaly_student(self):
		print(" this is a student")
class enginnering(student):
	def dispaly_enginnering(self):
		print("this is an enginnering student")
e=enginnering()
e.dispaly_person()
e.dispaly_student()
e.dispaly_enginnering()