def sical():
	print("enter principal")
	P=float(input())
	print("enter rate of interset")
	R=float(input())
	print("enter time")
	T=float(input())
	SI=P*R*T/100
	return SI
result=sical()
print("simple interest is:",result)