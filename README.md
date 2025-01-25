# AABBCD
<ins>A</ins>xis <ins>A</ins>ligned <ins>B</ins>ounding <ins>B</ins>ox for <ins>C</ins>ontinuous <ins>D</ins>istributions

## Description
This is a small package for computing the (approximate) domain of a numerical continuous distribution with arbitrary dimensionality. The goal is to return the smallest non-disjoint axis-aligned bounding box $\Omega$ such that\
$$\int_\Omega f(\mathbf{x}) d\mathbf{x} > 1 - \epsilon$$,\
where $f(\mathbf{x})$ is the distribution to be bounded, defined in any (possibly non-orthogonal) coordinate system, and assumed here to be normalized without loss of generalization (if $f(\mathbf{x})$ is *not* normalized, we bound $(1 - \epsilon)$\% of $f(\mathbf{x})$ in $\Omega$). $\epsilon$ is a user defined parameter that controls the tightness of the computed domain, and assumed to be a small ($\epsilon \ll 1$) positive number. This is useful when $f(\mathbf{x})$ is in some sense compact, *i.e.* a distribution with rapidly decaying tails (*e.g.* gaussian or laplace distributions) that are not important in subsequent computation.

## Algorithm
This package uses the algorithm described in the following paper:\
**COMING SOON**\
which was originally designed for computing the support of localized orbitals in a condensed phase system for later use in a linear-scaling exact exchange calculation. The computed bounds are provably large, but may not be the most compact solution. In practice, we find that they are quite good for many distributions (and provably good for radially-decaying 1D distributions).

The basic idea is to compress an $n$-D distribution into $n$ 1-D marginal distributions $f_{i}(x_{i}) = \int f(\mathbf{x}) d \mathbf{x_{j \neq i}}$. The bounds of $f_i(x_i)$ are computed using a simple algorithm that iteratively expands the marginal bounding box $\Omega_i$ to include grid points with the largest marginal density until $\int_{\Omega_i} f_{i}(x_{i}) d x_{i} > 1- (\epsilon/n)$. Then, the final $\Omega = \cap_i^n \Omega_i$ is constructed. All integrals are treated as simple Riemann sums.

## Installation
The AABBCD package requires numpy and python version >3.7. 

AABBCD is available on pypi *via* pip
```
pip install -i https://test.pypi.org/simple/ aabb-zacharysparrow
```
To test your installation... **COMING SOON**

## Instructions for Use
Once the package has been installed, using it is as simple as
```
from aabb-zacharysparrow import draw_aabb

draw_aabb(my_distribution, my_epsilon)
```
<tt>`my_distribution`</tt> must be an $n$-D numpy array, with entries equal to the distribution times the grid volume element -- $f(\mathbf{x})\Delta \mathbf{x}$.

If <tt>`my_distribution`</tt> is *not* normalized, the program will proceed anyway using $(1- \epsilon)* \left| f(\mathbf{x}) \right|$ as the bound. This is equivalent to ensuring $(1 - \epsilon)$\% of $f(\mathbf{x})$ is within $\Omega$ as described above.

The output of <tt>`draw_aabb()`</tt> is a dictionary containing the following items: <tt>`"bounds"`</tt>, <tt>`"norm"`</tt>, and <tt>`"distribution"`</tt>, which contain the indices of the input array corresponding to the axis-aligned bounding box bounds, the norm of the truncated distribution, and the truncated distribution itself, respectively. The truncated distribution is related to the input distribution *via* the bounds as
```
trancated_distribution = input_distribution[tuple(slice(b[0],b[1],1) for b in bounds)]
```

## Reference
If you use this package for your work, please cite the following reference:
**COMING SOON**

## TODO
- Add tests
- Upload to pypi
- Add reference
