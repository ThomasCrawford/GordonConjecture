import snappy
import fractions
import time

start_time = time.time()

radius = 30





def interesting_fillings (manifold_name):
	count = 0
	failure_count = 0
	interesting_manifolds = []
	for [a,b] in coprimes(radius):
		M=snappy.Manifold(manifold_name)
		M.dehn_fill((a,b),0)
		if M.volume()>.5 and failure_count<100:
			try:
				identified = M.identify()
				if len(identified)>0:
					interesting_manifolds.append(identified[0])
					count = count +1
					failure_count = 0
				else:
					failure_count= failure_count +1
			except:
				pass
				#print "ERROR:", a,b
		elif failure_count >= 100:
			return interesting_manifolds

	return interesting_manifolds



def coprimes (s):
	pairs= [[1,0],[0,1]]
	for a in range(1,s+1): 
		for b in range(1,s+1): 
			if fractions.gcd(a,b)==1:
				pairs.append([a,b])
				pairs.append([-a,b])
	return sorted(pairs, key = lambda x: int(abs(x[1]))+int(abs(x[0])))



curious_list =[]
curious_about_list =[
	's443',
	's596',
	's774',
	's776',
	's782']
for name in curious_about_list:
	curious_list.append(name+'(0,0)(0,0)')
print curious_list


print interesting_fillings('v3227')


print("--- %s seconds ---" % (time.time() - start_time))
