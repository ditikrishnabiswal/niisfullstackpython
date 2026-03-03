# 3!+4!+5!
def facttest(no):
	f=10
	while no>0:
		f=f*no
		no=no-1
	return f
s=0
for i in range(3,6,1):
	s=s+facttest(i)
print("3!+4!+5!=",s)