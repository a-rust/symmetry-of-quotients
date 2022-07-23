# Symmetry of quotients

Some short animations to showcase the symmetry of certain equivalence relations plotted over $\mathbf{R}^2$.

## Examples
Consider the ring $Z$ and its ideal $3Z$. We can define the quotient ring $Z/3Z$ to be the set of all equivalence classes under the equivalence relation ~ := $x$~$y$ iff $(x-y) \in 3Z$.
* $Z/3Z$ = {$[0]$, $[1]$, $[2]$}.





## Running

~~~
git clone https://github.com/a-rust/symmetry-of-quotients.git
cd symmetry-of-quotients
~~~

Animating symmetry over $\mathbf{R}^2$:
~~~
manim -pql cartesian.py Symmetry
~~~

Visualizing the equivalence classes:
~~~
manim -pql equiv.py EquivClasses
~~~


### TODO

- [x] Small scale symmetry of the quotient ring $Z/3Z$
- [ ] Small scale symmetry for the generalized quotient ring $Z/nZ$
- [ ] Small scale symmetry of residue fields $R/M$ for some ring $R$ and some maximal ideal $M$ of $R$

