import numpy
from matplotlib import pyplot

overs = numpy.array([1,2,3,4,5,6,7,8,9])
runs = numpy.array([36,12,4,6,0,12,10,10,2])

pyplot.bar(overs,runs)
pyplot.show()
