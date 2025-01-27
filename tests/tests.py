import sys
sys.path.append("../src/aabbcd")

from aabb import draw_aabb
import numpy as np
import math
from scipy.stats import multivariate_normal

print("Test case 1")
epsilon = 0.2
test_input = 2.0*np.array([0.0,0.0,0.01,0.02,0.04,0.08,0.16,0.38,0.16,0.08,0.04,0.02,0.01,0.0,0.0,0.0,0.0])
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[5, 10]]), "Failed test 1"
print("...ok")
print("")

print("Test case 2")
epsilon = 0.2
test_input = np.array([[0.0,0.0,0.02,0.0,0.0],[0.0,0.04,0.08,0.04,0.0],[0.04,0.06,0.10,0.08,0.04],[0.04,0.06,0.10,0.08,0.04],[0.0,0.04,0.08,0.04,0.0],[0.0,0.0,0.02,0.0,0.0]])
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[1, 5],[1, 5]]), "Failed test 2"
print("...ok")
print("")

print("Test case 3")
epsilon = 0.2
test_input = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.9,0.1,0.0])
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[6, 7]]), "Failed test 3"
print("...ok")
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
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm"]])
assert(my_aabb["bounds"] == [[87, 113],[87, 113]]), "Failed test 4"
print("...ok")
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
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm"]])
assert(my_aabb["bounds"] == [[8, 15], [9, 16], [8, 15], [7, 14], [8, 15]]), "Failed test 5"
print("...ok")
print("")

print("Test case 6")
epsilon = 0.21
test_input = np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,1,1,1,0,0])/10
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[11, 18]]), "Failed test 6"
print("...ok")
print("")

print("Test case 7")
epsilon = 0.1
test_input = np.array([1.0])
my_aabb = draw_aabb(test_input, epsilon)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[0, 1]]), "Failed test 7"
print("...ok")
print("")

print("Test case 8")
epsilon = 0.1
test_input = np.array([0.0])
try:
    my_aabb = draw_aabb(test_input, epsilon)
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed test 8")
except:
    print("...ok")
    print("")

print("Test case 9")
epsilon = 0.1
test_input = np.array([0.0,0.0,0.1,-0.1,0.01,0.02,0.04,0.08,0.16,0.38,0.16,0.08,0.04,0.02,0.01,0.0,0.0,0.0,0.0])
try:
    my_aabb = draw_aabb(test_input, epsilon)
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed test 9")
except:
    print("...ok")
    print("")

print("Test case 10")
epsilon = 0.1
test_input = np.array([])
try:
    my_aabb = draw_aabb(test_input, epsilon)
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed test 10")
except:
    print("...ok")
    print("")

print("Test case 11")
epsilon = 1.0
test_input = np.array([0.0,0.2,0.3,0.3,0.2,0.0])
my_aabb = draw_aabb(test_input, epsilon)
assert(my_aabb["bounds"] == [[]]), "Failed test 11"
print("...ok")
print("")

print("Test case 12")
epsilon = 0.0
test_input = np.array([0.0,0.2,0.3,0.3,0.2,0.0])
my_aabb = draw_aabb(test_input, epsilon)
assert(my_aabb["bounds"] == [[1, 5]]), "Failed test 12"
print("...ok")
print("")
