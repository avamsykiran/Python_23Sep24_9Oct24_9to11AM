from scipy import interpolate
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interpolate.interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)