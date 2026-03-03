def facttest(no):
	f=1
	while no>0:
		f=f*no
		n=no-1
	print("factorial=",f)
print("enter a number")
no=int(input())
facttest(no)