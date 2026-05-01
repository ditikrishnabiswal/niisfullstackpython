#string element stored in list
s="welcome"
L=[]
for i in s:
	if i not in L:
		L.append(i)
print(L)