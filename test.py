import snappy
# import hikmot
import cmath

M= snappy.Manifold ('s780(0,0)(0,1)')
N = snappy.Manifold('m004')
print M.is_isometric_to(N)