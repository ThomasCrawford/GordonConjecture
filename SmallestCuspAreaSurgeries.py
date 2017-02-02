import snappy
import fractions

manifold_name = 'v3376'

s=16

M=snappy.Manifold(manifold_name)
cusp = M.cusp_neighborhood()		
cusp.set_displacement(100)
print cusp.volume()


pairs= [[1,0],[0,1]]
for a in range(1,s+1): 
	for b in range(1,s+1): 
		if fractions.gcd(a,b)==1:
			pairs.append([a,b])
			pairs.append([-a,b])


M=snappy.Manifold(manifold_name)
cusp = M.cusp_neighborhood()


new_maifolds= []

cannot_cusp =[]

for [a,b] in pairs:
	M=snappy.Manifold(manifold_name)
	M.dehn_fill((a,b),0)
	if M.volume()>.5:
		try:
			cusp = M.cusp_neighborhood()		
			cusp.set_displacement(100)
			new_maifolds.append([[a,b],cusp.volume()])
			#new_maifolds.append([[a,b],M,M.identify(),cusp.volume()])
		except RuntimeError:
			cannot_cusp.append([a,b])
	else:
		new_maifolds.append([[a,b],False])


new_maifolds.sort(key=lambda x: x[-1])

for item in new_maifolds:
	print item

print '-------------'

print cannot_cusp
