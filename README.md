# AABBCD
<ins>A</ins>xis <ins>A</ins>ligned <ins>B</ins>ounding <ins>B</ins>ox for <ins>C</ins>ompact <ins>D</ins>istributions

## Description
This is a small package for computing the (approximate) domain of a numerical distribution with arbitrary dimensionality. The goal is to return the smallest non-disjoint axis-aligned bounding box $\Omega$ such that\
$$\int_\Omega f(\mathbf{x}) d\mathbf{x} > 1 - \epsilon$$,\
where $f(\mathbf{x})$ is the distribution to be bounded, defined in any (possibly non-orthogonal) coordinate system, and assumed here to be normalized without loss of generalization (if $f(\mathbf{x})$ is *not* normalized, we bound $(1 - \epsilon)$\% of $f(\mathbf{x})$ in $\Omega$). $\epsilon$ is a user defined parameter that controls the tightness of the computed domain, and assumed to be a small ($\epsilon \ll 1$) positive number. This is useful when $f(\mathbf{x})$ is in some sense compact, *i.e.* a distribution with rapidly decaying tails (*e.g.* gaussian or laplace distributions) that are not important in subsequent computation.

## Algorithm
This package uses the algorithm described in the following paper:\
**COMING SOON**\
which was originally designed for computing the support of localized orbitals in a condensed phase system for later use in a linear-scaling exact exchange calculation. The computed bounds are provably large, but may not be the most compact solution. In practice, we find that they are quite good for many distributions (and provably good for radially-decaying 1D distributions).

The basic idea is to compress an $n$-D distribution into $n$ 1-D marginal distributions $f_{i}(x_{i}) = \int f(\mathbf{x}) d \mathbf{x_{j \neq i}}$. The bounds of $f_i(x_i)$ are computed using a simple algorithm that iteratively expands the marginal bounding box $\Omega_i$ to include grid points with the largest marginal density until $\int_{\Omega_i} f_{i}(x_{i}) d x_{i} > 1- (\epsilon/n)$. Then, the final $\Omega = \cap_i^n \Omega_i$ is constructed. All integrals are treated as simple Riemann sums.

## Installation
The AABBCD package requires numpy (tested with version >2.2) and python (teseted with version >3.7). Some tests require scipy (tested with version >1.15) for loading distributions.

AABBCD is available on pypi *via* pip
```
pip install -i https://test.pypi.org/simple/ aabb-zacharysparrow
```
To test your installation, run tests/test.py (requires scipy).

## Instructions for Use
Once the package has been installed, using it is as simple as
```
import aabbcd as aabb

aabb.draw_aabb(my_distribution, my_epsilon)
```
<tt>`my_distribution`</tt> must be an $n$-D numpy array, with entries equal to the distribution times the grid volume element -- <tt>`my_distribution[i,j,...]`</tt> $= f(\mathbf{x_{i,j,...}})\Delta \mathbf{x_{i,j,...}}$.

If <tt>`my_distribution`</tt> is *not* normalized, the program will proceed anyway using $(1- \epsilon)* \left| f(\mathbf{x}) \right|$ as the bound. This is equivalent to ensuring $(1 - \epsilon)$\% of $f(\mathbf{x})$ is within $\Omega$ as described above.

The output of <tt>`draw_aabb()`</tt> is either a list containing the distribution bounds, or if the verbose option is used, a dictionary containing the following items: <tt>`"bounds"`</tt>, <tt>`"norm"`</tt>, and <tt>`"distribution"`</tt>, which contain the indices of the input array corresponding to the axis-aligned bounding box bounds, the norm of the truncated distribution, and the truncated distribution itself, respectively. The truncated distribution can be computed using the bounds as
```
trancated_distribution = aabb.trunc_dist[distribution, bounds].
```

Other functions that might be useful are
```
aabb.marginalize(distribution, axis)
```
which marginalizes a distribution, and
```
aabb.marginal_bound(marginal_distribution, epsilon)
```
which bounds a marginal distribution using the tightness parameter epsilon.

For more details, please see the given tests, which also serve as useful examples.

## Reference
If you use this package for your work, please cite the following reference:\
**COMING SOON**

## TODO
- Upload to pypi
- Add reference
- Make sure tests use pypi package 
