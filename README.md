# jsymb
Compute the symbol of the jones polynomial symbol of a chord diagram. That's the coefficient of the modified Jones polynomial (the Jones polynomial in $$h$$ where $$h = e^{q}$$) that depends only on the chord diagram of a singular knot. If the knot has $$n$$ double points, it's the coefficient of $$h^{n}$$.

### Usage

`python jsymb.py <code>`

The `code` argument is a collection of symbols corresponding to the labels of the arcs, when read around the chord diagram.

e.g.
```
python jsymb.py 121323
> -6
```

