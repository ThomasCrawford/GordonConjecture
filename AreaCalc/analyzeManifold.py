import snappy
import hikmot
import cmath
import fractions
from termcolor import colored

print colored('hello', 'red'), colored('world', 'green')


twoCuspMfld = 's647'
r = 6

def reformatNumber ( snappyNumber ):
	imag = float(snappyNumber.imag())
	real = float(snappyNumber.real())
	return real + imag*1j

def coprimes (s, xTranslation, yTranslation):
	pairs= [[1,0],[0,1]]
	for a in range(1,s+1): 
		for b in range(1,s+1): 
			if fractions.gcd(a,b)==1:
				pairs.append([a,b])
				pairs.append([-a,b])
	return sorted(pairs, key = lambda x: float(abs(x[1]))+float(abs(x[0])))
	# return sorted(pairs, key = lambda x: float(abs(x[1]))+float(abs(x[0])))

M = snappy.Manifold(twoCuspMfld)
print M.identify()
C=M.cusp_neighborhood()

yFristTranslation = reformatNumber(C.all_translations()[0][0])
xFirstTranslation = reformatNumber(C.all_translations()[0][1])

surgeryLength = abs(2*yFristTranslation+3*xFirstTranslation)
print type(surgeryLength)

 
greaterThan = []
lessThan = []
notHyp = []
miss = []

for [i,j] in coprimes(r , xFirstTranslation, yFristTranslation):
	# print i,j
	M = snappy.Manifold(twoCuspMfld)
	M.dehn_fill((i,j),0)
	if M.volume() > 0.5:
		try:
			C = M.cusp_neighborhood()
			C.set_displacement(100)
			surgeryLength = abs(i*yFristTranslation+j*xFirstTranslation)
			cuspArea = C.volume()*2
			if C.volume()<2.621:
				print "{0:.3f}".format(surgeryLength) + '   ' + colored(cuspArea, 'green')
				lessThan.append((i,j))
			else: 
				print "{0:.3f}".format(surgeryLength) + '   ' + colored(cuspArea, 'red')
				greaterThan.append((i,j))
		except:
			print 'Failed to construct cusp for ' + str((i,j)) +' surgery' 
			miss.append((i,j))
			pass
	else: 
		print str((i,j)) + ' surgery is not hyperbolic'
		notHyp.append((i,j))

print 'Under cutoff: ' + str(len(lessThan))
print 'Over cutoff: ' + str(len(greaterThan))
print 'Not Hyperbolic: ' + str(len(notHyp))
print 'Could not construct cusp: ' + str(len(miss))



