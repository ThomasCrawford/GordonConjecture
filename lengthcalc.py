import snappy
import hikmot

mani = 's782'

manifold = snappy.Manifold(mani)



#given cusp translation shapes, this finds all curves of lenght less than 6
def twocuspsgethypcurves (manifold):

	m=manifold.cusp_translations()[0][0]
	l=manifold.cusp_translations()[0][1]
	pairs = []
	shortcurves= []

	pairs.append([1,0])
	for y in range(2,7):
		pairs.append([1,y])
		pairs.append([-1,y])
	for x in range(-7,7):
		pairs.append([x,1])
		for y in range (2,7):
			if x%y != 0 and y%x !=0:
				pairs.append([x,y])


	for [x,y] in pairs:
		if abs(x*l+y*m)<6:
			shortcurves.append([x,y])


	hypshortcurves = []
	nonhypshortcurves = []

	for [a,b] in shortcurves:
		M=snappy.Manifold(mani)
		M.dehn_fill((a,b),0)
		if hikmot.verify_hyperbolicity(M,False)[0]:
			hypshortcurves.append([a,b])
		else:
			nonhypshortcurves.append((a,b))
	print 'non hyp:'
	print nonhypshortcurves
	return hypshortcurves



def onecuspgetexc (a,b,manifold):

	m=manifold.cusp_translations()[0][0]
	l=manifold.cusp_translations()[0][1]
	pairs = []
	shortcurves= []

	pairs.append([1,0])
	for y in range(2,7):
		pairs.append([1,y])
		pairs.append([-1,y])
	for x in range(-7,7):
		pairs.append([x,1])
		for y in range (2,7):
			if x%y != 0 and y%x !=0:
				pairs.append([x,y])

	for [x,y] in pairs:
		if abs(x*l+y*m)<6:
			shortcurves.append([x,y])
	hypshortcurves = []
	nonhypshortcurves = []
	for [c,d] in shortcurves:
		M=snappy.Manifold(mani)
		M.dehn_fill((a,b),0)
		M.dehn_fill((c,d),1)
		if hikmot.verify_hyperbolicity(M,False)[0]:
			hypshortcurves.append([a,b])
		else:
			nonhypshortcurves.append((c,d))
	return nonhypshortcurves



def getexecfromrealname (name):
	strname = str(name)
	pairs = []
	pairs.append([1,0])
	for y in range(2,7):
		pairs.append([1,y])
		pairs.append([-1,y])
	for x in range(-6,7):
		pairs.append([x,1])
		for y in range (2,7):
			if x%y != 0 and y%x !=0:
				pairs.append([x,y])

	hypshortcurves = []
	nonhypshortcurves = []
	for [c,d] in pairs:
		thismanifold= snappy.Manifold(strname)
		thismanifold.dehn_fill((c,d),0)
		#print thismanifold, hikmot.verify_hyperbolicity(thismanifold,False)[0]
		if hikmot.verify_hyperbolicity(thismanifold,False)[0]:
			hypshortcurves.append([c,d])
		else:
			nonhypshortcurves.append((c,d))
	return nonhypshortcurves
	


def unverifiedfromname (name):

	strname = str(name)
	pairs = []
	pairs.append([1,0])
	for y in range(2,7):
		pairs.append([1,y])
		pairs.append([-1,y])
	for x in range(-6,7):
		pairs.append([x,1])
		for y in range (2,7):
			if x%y != 0 and y%x !=0:
				pairs.append([x,y])

	hypshortcurves = []
	nonhypshortcurves = []
	for [c,d] in pairs:
		thismanifold= snappy.Manifold(strname)
		thismanifold.dehn_fill((c,d),0)
		#print thismanifold, hikmot.verify_hyperbolicity(thismanifold,False)[0]
		if thismanifold.volume() > 0.2:
			hypshortcurves.append([c,d])
		else:
			nonhypshortcurves.append((c,d))
	return nonhypshortcurves





onecusplist = twocuspsgethypcurves (snappy.Manifold(mani))

#multi methods (real name, dehn filling, etc)





#dehn filling name
for [a,b] in onecusplist:
	double = onecuspgetexc(a,b,snappy.Manifold(mani))

	M=snappy.Manifold(mani)
	M.dehn_fill((a,b),0)
	single = getexecfromrealname(M.identify()[0])

	combined = [val for val in double if val in single]

	print [a,b], len(combined)
	print '-------------'

'''
#dehn filling name

for [a,b] in onecusplist:
	print [a,b] , onecuspgetexc(a,b,snappy.Manifold(mani))


#real name 
realname = []
for [a,b] in onecusplist:
	M=snappy.Manifold(mani)
	M.dehn_fill((a,b),0)
	realname.append(M.identify()[0])
for name in realname:
	print name, (getexecfromrealname(name))
	print '-----------'

'''

'''
#real name  unverified
realname = []
for [a,b] in onecusplist:
	M=snappy.Manifold(mani)
	M.dehn_fill((a,b),0)
	realname.append(M.identify()[0])
for name in realname:
	print name, (unverifiedfromname(name))
	print '-----------'
'''


