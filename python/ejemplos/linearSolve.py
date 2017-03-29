#3 * x0 + x1 = 9 and x0 + 2 * x1 = 8

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
x

np.allclose(np.dot(a, x), b)