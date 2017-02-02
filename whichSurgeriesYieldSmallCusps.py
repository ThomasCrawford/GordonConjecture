import snappy
import hikmot
import cmath
import fractions

twoCuspMfld = 'v3376'
r = 20



def coprimes (s):
	pairs= [[1,0],[0,1]]
	for a in range(1,s+1): 
		for b in range(1,s+1): 
			if fractions.gcd(a,b)==1:
				pairs.append([a,b])
				pairs.append([-a,b])
	return sorted(pairs, key = lambda x: int(abs(x[1]))+int(abs(x[0])))

M = snappy.Manifold(twoCuspMfld)
# M.canonize()
print M.identify()
C = M.cusp_neighborhood()
C.set_displacement(100,0)
C.set_displacement(100,1)

yFristTranslation = C.all_translations()[0][0]
xFirstTranslation = C.all_translations()[0][1]

L= []

for [i,j] in coprimes(r):
	# print i,j
	M = snappy.Manifold(twoCuspMfld)
	if M.volume()>.5:
		M.dehn_fill((i,j),0)
		try:
			C = M.cusp_neighborhood()
			C.set_displacement(100)
			if C.volume()<2.621:
				length = abs(i*xFirstTranslation+j*yFristTranslation)
				# print length
				# print C.volume()
				L.append((i,j))
		except:
			print (i,j)
			pass

print L
print len(L)
for (a,b) in L:
	M=snappy.Manifold(twoCuspMfld)
	M.dehn_fill((a,b),0)
	print (a,b)
	print M.identify()




