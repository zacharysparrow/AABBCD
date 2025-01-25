import sys
#sys.path.append("/home/sparrow/Documents/data_projects/AABBCD/src/aabb_zacharysparrow")
sys.path.append("../src/aabb_zacharysparrow")

from aabb import draw_aabb
import numpy as np

test_input = np.array([0.0,0.0,0.01,0.02,0.04,0.08,0.16,0.38,0.16,0.08,0.04,0.02,0.01,0.0,0.0,0.0,0.0])
my_aabb = draw_aabb(test_input, 0.2)
print(my_aabb)

test_input_2 = np.array([[0.0,0.0,0.02,0.0,0.0],[0.0,0.04,0.08,0.04,0.0],[0.04,0.06,0.10,0.08,0.04],[0.04,0.06,0.10,0.08,0.04],[0.0,0.04,0.08,0.04,0.0],[0.0,0.0,0.02,0.0,0.0]])
my_aabb2 = draw_aabb(test_input_2, 0.2)
print(my_aabb2)
