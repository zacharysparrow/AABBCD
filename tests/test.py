import sys
#sys.path.append("/home/sparrow/Documents/data_projects/AABBCD/src/aabb_zacharysparrow")
sys.path.append("../src/aabb_zacharysparrow")

from aabb import draw_aabb
import numpy as np
import math
from scipy.stats import multivariate_normal

print("Test case 1")
epsilon = 0.2
test_input = 2.0*np.array([0.0,0.0,0.01,0.02,0.04,0.08,0.16,0.38,0.16,0.08,0.04,0.02,0.01,0.0,0.0,0.0,0.0])
print("Input norm:")
print(np.sum(test_input))
print("Input epsilon:")
print(epsilon)
my_aabb = draw_aabb(test_input, epsilon)
print([my_aabb[key] for key in ["bounds","norm"]])

print("")

print("Test case 2")
epsilon = 0.2
test_input = np.array([[0.0,0.0,0.02,0.0,0.0],[0.0,0.04,0.08,0.04,0.0],[0.04,0.06,0.10,0.08,0.04],[0.04,0.06,0.10,0.08,0.04],[0.0,0.04,0.08,0.04,0.0],[0.0,0.0,0.02,0.0,0.0]])
print("Input norm:")
print(np.sum(test_input))
print("Input epsilon:")
print(epsilon)
my_aabb = draw_aabb(test_input, epsilon)
print([my_aabb[key] for key in ["bounds","norm"]])
print("")

print("Test case 3")
epsilon = 0.2
test_input = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.9,0.1,0.0])
print("Input norm:")
print(np.sum(test_input))
print("Input epsilon:")
print(epsilon)
my_aabb = draw_aabb(test_input, epsilon)
print([my_aabb[key] for key in ["bounds","norm"]])
print("")

print("Test case 4")
epsilon = 0.02
rv = multivariate_normal([0.0, 0.0], [[1.0, 0.0], [0.0, 1.0]])
minpos = -20
maxpos = 20
spacing = 0.2
x, y = np.mgrid[minpos:maxpos:spacing, minpos:maxpos:spacing]
volume_element = spacing**2
pos = np.stack((x, y), axis=2)
test_input = np.array(volume_element*rv.pdf(pos))
print("Input norm:")
print(np.sum(test_input))
print("Input epsilon:")
print(epsilon)
my_aabb = draw_aabb(test_input, epsilon)
print([my_aabb[key] for key in ["bounds","norm"]])
print("")

print("Test case 5")
epsilon = 0.01
rv = multivariate_normal([0.0,1.0,0.0,-1.0,0.0],[[1.0,0.5,0.0,0.0,0.0],[0.5,1.0,0.5,0.0,0.0],[0.0,0.5,1.0,0.5,0.0],[0.0,0.0,0.5,1.0,0.5],[0.0,0.0,0.0,0.5,1.0]])
minpos = -10
maxpos = 10
spacing = 0.9
x1, x2, x3, x4, x5 = np.mgrid[minpos:maxpos:spacing, minpos:maxpos:spacing, minpos:maxpos:spacing, minpos:maxpos:spacing, minpos:maxpos:spacing]
volume_element = spacing**5
pos = np.stack((x1, x2, x3, x4, x5), axis=5)
test_input = np.array(volume_element*rv.pdf(pos))
print("Input norm:")
print(np.sum(test_input))
print("Input epsilon:")
print(epsilon)
my_aabb = draw_aabb(test_input, epsilon)
print([my_aabb[key] for key in ["bounds","norm"]])
print("")
