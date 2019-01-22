#file 2: lambd2.py
def myfunc(n):
	return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
dub = mydoubler(11)
trip = mytripler(11)

print("dub ", dub)
print("trip " ,trip)
