# AABBCD
Axis Aligned Bounding Box for Continuous Distributions

This is a small package for computing the (approximate) domain of a numerical continuous distribution with arbitrary dimensionality. The goal is to return the smallest non-disjoint axis-aligned bounding box $\Omega$ such that
$$
 \int_\Omega f(\bm x) \dd x > 1 - \epsilon,
$$
where $f(\bm x)$ is the distribution to be bounded, defined in any (possibly non-orthogonal) coordinate system. $\epsilon$ is a user defined parameter that controls the tightness of the computed domain, and assumed to be a small ($\epsilon \ll 1$) positive number. This is most useful when $f(x)$ is in some sense compact, *i.e.* a distribution with rapidly decaying tails (*e.g.* gaussian-like, laplace-like, or cauchy distributions) that are not important in subsequent computation.

This package uses the algorithm described in the following paper:
**COMING SOON**
which was originally designed for computing the support of localized orbitals in a condensed phase system for later use in a linear-scaling exact exchange calculation. The computed bounds are provably large, but may not be the most compact solution. In practice, we find that they are quite good for many distributions (and provably good for radially-decaying 1D distributions).

TODO:
- add instructions for use
- briefly describe the algorithm
- add instructions for installation and dependencies
