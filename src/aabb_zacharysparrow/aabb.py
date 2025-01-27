import numpy as np
import warnings

def draw_aabb(dist: np.ndarray, eps: float):

    if not isinstance(dist, np.ndarray):
        raise Exception("Input distribution is not a NumPy array.")
    dist_norm = np.sum(dist)
    if dist_norm != 1.0:
        warnings.warn("Warning! The input distribution is not well normalized. Proceeding anyway.")
        dist = dist/dist_norm
    if dist_norm == 0.0:
        raise Exception("Norm of input distribution is zero.")
    if np.any(dist < 0):
        raise Exception("The distribution array contains negative numbers.")
    if not isinstance(eps, float):
        raise Exception("Input epsilon is not a float.")
    if eps < 0.0 or eps > 1.0:
        raise Exception("Epsilon must be between 0 and 1.")

    dim = dist.ndim
    marginal_eps = eps / dim

    marginal_dists = [marginalize(dist, i) for i in range(dim)]
    bounds = [marginal_bound(d, marginal_eps) for d in marginal_dists]

    truncated_dist = trunc_dist(dist, bounds)
    truncated_norm = np.sum(truncated_dist)
    if truncated_norm < 1.0 - eps:
        print("WARNING! Something went wrong -- the norm of the truncated distribution is less than 1.0 - epsilon!")

    result = dict()
    result["bounds"] = bounds
    result["norm"] = truncated_norm*dist_norm
    result["distribution"] = truncated_dist*dist_norm

    return result


def marginalize(dist, axis):
    axes = tuple(x for x in range(dist.ndim) if x != axis)
    marginal = np.sum(dist, axis = axes)
    return marginal


def marginal_bound(dist, eps):
    cost_list = list(range(len(dist)))
    cost_list = [min(x, y) for x, y in zip(cost_list, list(reversed(cost_list)))] # add middle first
    dist_to_sort = np.array(list(zip(dist, cost_list)), dtype=[('dist', '<f8'),('cost', '<i8')])
    ordering = np.argsort(dist_to_sort, order=['dist','cost'], stable=True)[::-1]
    norm = 0
    lb = max(ordering)
    rb = min(ordering)
    i = 0
    while norm < 1.0 - eps:
        norm += dist[ordering[i]]
        lb = min(ordering[i], lb)
        rb = max(ordering[i], rb)
        i += 1
    return [lb.item(),(rb + 1).item()]


def trunc_dist(dist, bounds):
    index = tuple(slice(b[0],b[1],1) for b in bounds)
    truncated_dist = dist[index]
    return truncated_dist

