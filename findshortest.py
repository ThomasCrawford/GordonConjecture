m= .5 + 1.32287j
l= 2

def getshortcurves (mlength,llength):

	m=mlength
	l=llength
	xstart = -10
	xstop = 10
	ystop = 10

	pairs = []
	under6= []

	pairs.append([1,0])
	for y in range(2,ystop+1):
		pairs.append([1,y])
		pairs.append([-1,y])
	for x in range(xstart,xstop+1):
		pairs.append([x,1])
		for y in range (2,ystop+1):
			if x%y != 0 and y%x !=0:
				pairs.append([x,y])


	for [x,y] in pairs:
		if abs(x*l+y*m)<6:
			under6.append([x,y])
	return under6
