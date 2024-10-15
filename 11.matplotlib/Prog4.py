import numpy
from matplotlib import pyplot

months = ["Jan","Feb","Mar","Apr","May"]
sales = numpy.array([2000,1000,500,1000,1200])

pyplot.pie(sales,labels=months)
pyplot.show()
