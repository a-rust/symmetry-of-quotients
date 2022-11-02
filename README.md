# Symmetry of quotients

Just some short animations that attempt to visualize equivalence relations of qoutient rings, along with the symmetry of what a complete graph of elements in each equivalence class (as the set of vertices) would look like.

This is just a random mini-project to get a feel for how the Manim animation engine works.

## Example
Consider the ring $\mathbb{Z}$ and its ideal $3\mathbb{Z}$. We can define the quotient ring $\mathbb{Z}/3\mathbb{Z}$ to be the set of all equivalence classes under the equivalence relation $R$ as follows: 

```math
R := \{(x, y)\in\mathbb{Z}^2 : x-y \in 3\mathbb{Z}\}.
```

Thus,

```math
\mathbb{Z}/3\mathbb{Z} = \{[0], [1], [2]\}.
```

The first animation shows each equivalence class plotted over the Cartesian plane. If we consider the elements of each equivalence class to be the set of vertices in a graph $G$, then we can also define a unique edge between every pair of distinct vertices. This gives a complete graph for each equivalence class, which is also visualized in the first animation. 

The second animation just attempts to visualize how $\mathbb{Z}/3\mathbb{Z}$ is built from the equivalence relation $R$.



![symmetry](https://user-images.githubusercontent.com/107306810/180685772-8a24b79c-1a6e-4671-8410-25ec30f91ca5.gif)
---

![equiv_classes](https://user-images.githubusercontent.com/107306810/180686044-adc261b6-e631-4d17-bcb7-2e17061e2201.gif)
---

## Running

~~~
git clone https://github.com/a-rust/symmetry-of-quotients.git
cd symmetry-of-quotients
~~~

First animation
~~~
manim -pql cartesian.py Symmetry
~~~

Second animation
~~~
manim -pql equiv.py EquivClasses
~~~


### TODO

- [x] Small scale symmetry of the quotient ring $Z/3Z$
- [ ] Small scale symmetry for the generalized quotient ring $Z/nZ$
- [ ] Small scale symmetry of residue fields $R/M$ for some ring $R$ and some maximal ideal $M$ of $R$

