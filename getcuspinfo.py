import snappy
import numpy

M=snappy.Manifold('v1902')

'''
covers = Manifold.covers(3)

M=covers[11]

'''


cusp = M.cusp_neighborhood()		
cusp.set_displacement(100)

print cusp.volume()*2
print cusp.translations()
