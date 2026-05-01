#wap initlize no 125 count no digit.
no=-125
if no<0:
	no=-no
c=0
while no!=0:
	no=no//10
	c=c+1
print("no of digit=",c)