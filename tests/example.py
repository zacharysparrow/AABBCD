import sys
sys.path.append("../src/aabbcd")

import aabb as aabb
import numpy as np
import math
from scipy.stats import multivariate_normal
import random

import time
import matplotlib.pyplot as plt

random.seed(42)

# Generate distributions
distribution_grid_size = 10
distributions = []
coords = []
for x in range(distribution_grid_size):
    for y in range(distribution_grid_size):
        x_rand, y_rand = [random.random(), random.random()]
        coords.append([x + x_rand, y + y_rand])
        dist = multivariate_normal([x + x_rand, y + y_rand],[[0.5,0.0],[0.0,0.5]])
        distributions.append(dist)

n_distributions = len(distributions)

# Generate grid
quadrature_spacing = 0.1
quadrature_padding = 4
minpos = 0 - quadrature_padding
maxpos = distribution_grid_size + quadrature_padding
x1, x2 = np.mgrid[minpos:maxpos:quadrature_spacing, minpos:maxpos:quadrature_spacing]
volume_element = quadrature_spacing**2
pos = np.stack((x1, x2), axis=2)

# Compute AABBs
start_time = time.time()
epsilon = 0.01
aabbs = []
for d in distributions:
    d_on_grid = np.array(volume_element*d.pdf(pos))
    d_aabb = aabb.draw_aabb(d_on_grid, epsilon)
    aabbs.append(d_aabb)

# Compute approximate s
s_approx = np.full((n_distributions, n_distributions), 0.0)
for i,bi in enumerate(aabbs):
    for j,bj in enumerate(aabbs):
        if i >= j:
            int_bounds = aabb.aabb_intersection(bi, bj)
            if int_bounds != None:
                trunc_i = aabb.trunc_dist(np.array(volume_element*distributions[i].pdf(pos)), int_bounds)
                trunc_j = aabb.trunc_dist(np.array(volume_element*distributions[j].pdf(pos)), int_bounds)
                s_approx[i,j] = np.sum(trunc_i * trunc_j)
                s_approx[j,i] = s_approx[i,j]
end_time = time.time()
print("Approx. Timing:")
print(end_time - start_time)

plt.imshow(s_approx, cmap='viridis')
plt.colorbar()
plt.title('Approx. S')
plt.show()

# Compute exact numerical s
start_time = time.time()
s_exact = np.full((n_distributions, n_distributions), 0.0)
for i,bi in enumerate(aabbs):
    for j,bj in enumerate(aabbs):
        if i >= j:
            di = np.array(volume_element*distributions[i].pdf(pos))
            dj = np.array(volume_element*distributions[j].pdf(pos))
            s_exact[i,j] = np.sum(di * dj)
            s_exact[j,i] = s_exact[i,j]
end_time = time.time()
print("Exact Timing")
print(end_time - start_time)

plt.imshow(s_exact - s_approx, cmap='viridis')
plt.colorbar()
plt.title('S error')
plt.show()
