import snappy
import hikmot


Ms = []
Fails = []

r = 4

for i in range(-r,r):
	for j in range (1,r):

		M = snappy.Manifold('s785')
		M.dehn_fill((i,j),0)
		if   hikmot.verify_hyperbolicity(M,False)[0]:
			Ms.append(M)
		else: Fails.append(M)

for i in range(-r,r):
	for j in range (1,r):

		M = snappy.Manifold('s785')
		M.dehn_fill((i,j),1)
		if   hikmot.verify_hyperbolicity(M,False)[0]:
			Ms.append(M)
		else: Fails.append(M)
print 'Hyperbolic:'
print len(Ms)
print Ms
print 'Test Failed'
print len(Fails)
print Fails



