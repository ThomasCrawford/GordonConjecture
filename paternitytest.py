import snappy
import fractions
import time

start_time = time.time()

#maximum value of a dehn filling, shouldn't get this far
radius = 6

main_dictionary = {}

#given a manifold and a specified cusp, returns all census manifolds which can be gotten by dehn filling on said cusp
def interesting_fillings (manifold_name, which_cusp):
	count = 0
	failure_count = 0
	interesting_manifolds = {}
	for [a,b] in coprimes(radius):
		M=snappy.Manifold(manifold_name)
		M.dehn_fill((a,b),which_cusp)
		if M.volume()>.5 and failure_count<100:
			try:
				identified = M.identify()
				if len(identified)>0:
					interesting_manifolds[str(identified[0])] = (a,b)
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


#gets a list of dehn fillings to try, ordered by sum of abs of integers
def coprimes (s):
	pairs= [[1,0],[0,1]]
	for a in range(1,s+1): 
		for b in range(1,s+1): 
			if fractions.gcd(a,b)==1:
				pairs.append([a,b])
				pairs.append([-a,b])
	return sorted(pairs, key = lambda x: int(abs(x[1]))+int(abs(x[0])))


def children (manifold):
	M=snappy.Manifold(manifold)
	for cusp_num in range(M.num_cusps()):
		kids=(interesting_fillings(manifold,cusp_num))
		for name in inquire_list:
			if name in kids:
				print str(name) + ' is ' + str(kids[name]) +' surgery on ' + manifold + ' cusp number ' +str(cusp_num)




#specify the children you want to know the parents of 
inquire_list =[
	's443(0,0)(0,0)',
	's596(0,0)(0,0)',
	's774(0,0)(0,0)',
	's776(0,0)(0,0)(0,0)',
	's782(0,0)(0,0)',
	's785(0,0)(0,0)',
	's647(0,0)(0,0)',
	's780(0,0)(0,0)',
	'm125(0,0)(0,0)',
	'm129(0,0)(0,0)',
	'm203(0,0)(0,0)',
	'm292(0,0)(0,0)',
	'm295(0,0)(0,0)',
	'v2533(0,0)(0,0)',
	'v2644(0,0)(0,0)',
	'v3211(0,0)(0,0)',
	'v3376(0,0)(0,0)']

# inquire_list=[
# 	'm034(0,0)'
# 	's572(0,0)'
# 	'm285(0,0)'
# 	]



parents=[]
for M in snappy.OrientableCuspedCensus[1000:8000]: 
	if M.num_cusps() >=2: 
		parents.append(str(M))

for parent in parents:
	children(parent)



print("--- %s seconds ---" % (time.time() - start_time))
