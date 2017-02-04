import snappy
import hikmot
import cmath
import fractions

mList = [
	'm125', 'm129', 'm203', 'm292', 'm295', 
	's596',	's647',	's774',	's776', 's780',	's782',	's785',
	'v2124', 'v2355', 'v2533', 'v2644', 'v2731', 'v3108', 'v3127', 'v3211', 'v3376'
]

for m in mList:
	print m
	M = snappy.Manifold(m)
	for cuspNum in range(M.num_cusps()):
		C = M.cusp_neighborhood()
		C.set_displacement(100, cuspNum)
		area = 2*C.volume(cuspNum)
		print ' cusp number ' + str(cuspNum) + ' has area ' + str(area)