import snappy
import hikmot
import cmath
import fractions


twoCuspMfld = 's647'

M = snappy.Manifold(twoCuspMfld)
C=M.cusp_neighborhood()

yFristTranslation = C.all_translations()[0][0]

# print type (3.0 + 2*1j)

# print type(complex(str(yFristTranslation)))



def reformatNumber ( snappyNumber ):
	imag = float(snappyNumber.imag())
	real = float(snappyNumber.real())
	return real + imag*1j

print type(yFristTranslation)
print type(reformatNumber(yFristTranslation))