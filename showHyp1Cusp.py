import snappy
import hikmot
import cmath

# oneCuspMfld = 'm038'
oneCuspMfld = 's785(0,0)(10,1)'


M = snappy.Manifold(oneCuspMfld)
# M.canonize()
print M.identify()
C = M.cusp_neighborhood()
C.set_displacement(100,0)
yTranslation = C.all_translations()[0][0]
xTranslation = C.all_translations()[0][1]
print yTranslation
print xTranslation
print C.volume()*2



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
		if abs(x*l+y*m)<6.2:
			under6.append((x,y))
	return under6


surgeryList = getshortcurves(xTranslation, yTranslation)


succeeds = []
fails = []

for surgery in surgeryList:
	M = snappy.Manifold(oneCuspMfld)
	M.dehn_fill(surgery,0)
	if hikmot.verify_hyperbolicity(M,False)[0]:
		succeeds.append(M)
	else: fails.append(M)

print 'Hyperbolic:'
print len(succeeds)
print succeeds
print 'Maybe Not Hyperbolic:'
print len(fails)
print fails



