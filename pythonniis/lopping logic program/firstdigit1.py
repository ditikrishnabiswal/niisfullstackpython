#wap initlize no 125 display first digit.
no=124
if no<0:
	no=-no
while no>=10:
	no=no//10
print("first digit=",no)
