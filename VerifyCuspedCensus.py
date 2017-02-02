# This is a python script to verify all manifolds in the cusped census. To show that a manifold is
# hyperbolic we only need to show that one triangulation of a given manifold is provably hyperbolic 
# by our method. In fact, we show that either the given triangulation of snappy is provably hyperbolic
# or the canonical triangulation is. Although with enough precision, one should be able to verify
# that all triangulations in the census are hyperbolic, checking either one is sufficient for our
# purposes.

import hikmot
import snappy


Census = snappy.OrientableCuspedCensus()
print snappy.OrientableCuspedCensus()

# print_data = 0
# save_data = 0

# GoodList=[]
# BadList=[]

# for M in snappy.OrientableCuspedCensus(): 
#     N = M.copy()
#     N.canonize()
#     print len(GoodList)

#     if  (hikmot.verify_hyperbolicity(N,False)[0] or hikmot.verify_hyperbolicity(M,False)[0]): # and M.is_isometric_to(N):
#         GoodList.append(N)
#     else:
#             BadList.append(N)
#             print " N=",N, " M=",M, " iso ", M.is_isometric_to(N), " hikmot ", hikmot.verify_hyperbolicity(M,print_data, save_data)[0] 



# print 'Out of', len(Census), ' manifolds in the OrientableCuspedCensus,', len(GoodList), ' have been proven to be hyperbolic and ', len(BadList), ' have not.'

