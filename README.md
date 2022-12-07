## Setup
Consider the qoutient ring $\mathbb{Z}/3\mathbb{Z}$.

If we consider the elements of each equivalence class $[x]$ (plotted below) to be the set of vertices in a graph $G_x$, and define an edge between every pair of distinct vertices in $G_x$, we get a complete graph, shown in the first animation.

The second animation just attempts to visualize how $\mathbb{Z}/3\mathbb{Z}$ is built through cosets.


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
