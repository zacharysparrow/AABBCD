import sys
sys.path.append("../src/aabbcd")

import aabb as aabb
import numpy as np
import math
from scipy.stats import multivariate_normal

print("Unit testing...")
test_dist = np.array([[1,1],[2,2]])
marginal_test_1 = aabb.marginalize(test_dist, 0)
marginal_test_2 = aabb.marginalize(test_dist, 1)
assert((marginal_test_1 == np.array([2,4])).all()), "Marginalization failed"
assert((marginal_test_2 == np.array([3,3])).all()), "Marginalization failed"
test_dist = np.array([0.0,1.0,2.0,1.0,0.0])
marginal_test_1 = aabb.marginalize(test_dist, 0)
assert((marginal_test_1 == test_dist).all()), "1D marginalization failed"
try:
    aabb.marginalize(test_dist, 2)
    raise AssertionError("")    
except AssertionError:
    raise AssertionError("Failed check that marginalization axis is reasonable")
except:
    pass

test_dist = np.array([0,1,2,3,4,5,4,3,2,1,0,0,0,0])/25
bound_test = aabb.marginal_bound(test_dist, 0.1)
assert(bound_test == [2, 9]), "Marginal bounding failed"
test_dist = np.array([0,0,0,0,0,0,0,1,1,1,1,1,1,2,1,1,0,0])/10
bound_test = aabb.marginal_bound(test_dist, 0.25)
assert(bound_test == [9, 16]), "Marginal bounding failed with nearly flat distribution"
test_dist = np.array([0,0,0,0,0,0,0,1,1,1,1,1,1,2,1,1,0,0])
bound_test = aabb.marginal_bound(test_dist, 0.25)
assert(bound_test == [9, 16]), "Marginal bounding failed with unnormalized distribution"
bound_test = aabb.marginal_bound(test_dist, 0.0)
assert(bound_test == [7, 16]), "Marginal bounding failed with eps=0.0"
bound_test = aabb.marginal_bound(test_dist, 1.0)
assert(bound_test == []), "Marginal bounding failed with eps=1.0"

test_dist = np.array([[1,2,3,4],[5,6,7,8]])
trunc_test = aabb.trunc_dist(test_dist, [[0,1],[0,3]])
assert((trunc_test == [[1,2,3]]).all()), "dist truncation failed"
try:
    trunc_test = aabb.trunc_dist(test_dist, [[0,3],[0,1]])
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed check that bounds are right size")
except:
    pass
try:
    trunc_test = aabb.trunc_dist(test_dist, [[0,1,1],[0,3]])
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed check that bounds are right length")
except:
    pass
try:
    trunc_test = aabb.trunc_dist(test_dist, [[2,0],[0,3]])
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed check that bounds are right order")
except:
    pass
try:
    trunc_test = aabb.trunc_dist(test_dist, [[0,1]])
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed check that bounds and dist have same dimensionality")
except:
    pass
print("All unit tests passed!")
print("")

print("Functional testing...")
print("Test case 1")
epsilon = 0.2
test_input = 2.0*np.array([0.0,0.0,0.01,0.02,0.04,0.08,0.16,0.38,0.16,0.08,0.04,0.02,0.01,0.0,0.0,0.0,0.0])
my_aabb = aabb.draw_aabb(test_input, epsilon, verbose=True)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[5, 10]]), "Failed test 1"
print("...ok")

print("Test case 2")
epsilon = 0.2
test_input = np.array([[0.0,0.0,0.02,0.0,0.0],[0.0,0.04,0.08,0.04,0.0],[0.04,0.06,0.10,0.08,0.04],[0.04,0.06,0.10,0.08,0.04],[0.0,0.04,0.08,0.04,0.0],[0.0,0.0,0.02,0.0,0.0]])
my_aabb = aabb.draw_aabb(test_input, epsilon, verbose=True)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[1, 5],[1, 5]]), "Failed test 2"
print("...ok")

print("Test case 3")
epsilon = 0.2
test_input = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.9,0.1,0.0])
my_aabb = aabb.draw_aabb(test_input, epsilon, verbose=True)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[6, 7]]), "Failed test 3"
print("...ok")

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
my_aabb = aabb.draw_aabb(test_input, epsilon)
#print(my_aabb)
assert(my_aabb == [[87, 113],[87, 113]]), "Failed test 4"
print("...ok")

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
my_aabb = aabb.draw_aabb(test_input, epsilon)
#print(my_aabb)
assert(my_aabb == [[8, 15], [9, 16], [8, 15], [7, 14], [8, 15]]), "Failed test 5"
print("...ok")

print("Test case 6")
epsilon = 0.21
test_input = np.array([0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,1,1,1,0,0])/10
my_aabb = aabb.draw_aabb(test_input, epsilon, verbose=True)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[11, 18]]), "Failed test 6"
print("...ok")

print("Test case 7")
epsilon = 0.1
test_input = np.array([1.0])
my_aabb = aabb.draw_aabb(test_input, epsilon, verbose=True)
#print([my_aabb[key] for key in ["bounds","norm","distribution"]])
assert(my_aabb["bounds"] == [[0, 1]]), "Failed test 7"
print("...ok")

print("Test case 8")
epsilon = 0.1
test_input = np.array([0.0])
try:
    my_aabb = aabb.draw_aabb(test_input, epsilon)
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed test 8")
except:
    print("...ok")

print("Test case 9")
epsilon = 0.1
test_input = np.array([0.0,0.0,0.1,-0.1,0.01,0.02,0.04,0.08,0.16,0.38,0.16,0.08,0.04,0.02,0.01,0.0,0.0,0.0,0.0])
try:
    my_aabb = aabb.draw_aabb(test_input, epsilon)
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed test 9")
except:
    print("...ok")

print("Test case 10")
epsilon = 0.1
test_input = np.array([])
try:
    my_aabb = aabb.draw_aabb(test_input, epsilon)
    raise AssertionError("")
except AssertionError:
    raise AssertionError("Failed test 10")
except:
    print("...ok")

print("Test case 11")
epsilon = 1.0
test_input = np.array([0.0,0.2,0.3,0.3,0.2,0.0])
my_aabb = aabb.draw_aabb(test_input, epsilon)
assert(my_aabb == [[]]), "Failed test 11"
print("...ok")

print("Test case 12")
epsilon = 0.0
test_input = np.array([0.0,0.2,0.3,0.3,0.2,0.0])
my_aabb = aabb.draw_aabb(test_input, epsilon)
assert(my_aabb == [[1, 5]]), "Failed test 12"
print("...ok")
print("All functional tests passed!")
