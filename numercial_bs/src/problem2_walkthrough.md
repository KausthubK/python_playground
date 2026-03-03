# Problem 2 Walkthrough: Cosine Similarity Matrix (NumPy)

## The Formula

```
cos_sim(u, v) = (u . v) / (||u|| * ||v||)
```

- `u . v` — **dot product**: multiply corresponding elements and sum. `[1,2] . [3,4] = 1*3 + 2*4 = 11`
- `*` — **scalar multiplication**: multiplying two single numbers together
- `||u||` — **L2 norm** (Euclidean length): `sqrt(u1² + u2² + ... + un²)`. So `||[3,4]|| = 5`

The result is a **scalar** between -1 and 1. But the problem asks for this computed for **every pair of rows**, producing an NxN matrix.

## Visualising Input/Output

```
X = [[1, 0],    <- row 0: points right
     [0, 1],    <- row 1: points up
     [1, 1]]    <- row 2: points diagonal

Output (3x3):
                 row 0    row 1    row 2
              ┌────────┬────────┬────────┐
    row 0     │  1.0   │  0.0   │  0.707 │
              ├────────┼────────┼────────┤
    row 1     │  0.0   │  1.0   │  0.707 │
              ├────────┼────────┼────────┤
    row 2     │  0.707 │  0.707 │  1.0   │
              └────────┴────────┴────────┘
```

- Diagonal is always 1.0 (vector is identical to itself)
- Symmetric: `[i,j] == [j,i]`
- Orthogonal vectors (90°) → 0.0
- 45° apart → 1/√2 ≈ 0.707

## Vectorising the Numerator

`@` is Python's matrix multiplication operator. `X.T` is the transpose.

```
X         X.T          X @ X.T
(N, D)  @ (D, N)   =   (N, N)
```

Element `[i, j]` of the result is the dot product of row i and row j.

```
X = [[1, 0],      X.T = [[1, 0, 1],
     [0, 1],             [0, 1, 1]]
     [1, 1]]

X @ X.T = [[1*1+0*0, 1*0+0*1, 1*1+0*1],     [[1, 0, 1],
           [0*1+1*0, 0*0+1*1, 0*1+1*1],  =    [0, 1, 1],
           [1*1+1*0, 1*0+1*1, 1*1+1*1]]       [1, 1, 2]]
```

All pairwise dot products in one operation.

## Vectorising the Denominator (Outer Product)

An outer product takes two vectors and produces a matrix — every element of the first multiplied by every element of the second.

```
norms = [||row0||, ||row1||, ||row2||]   # shape (N,)

np.outer(norms, norms):

         n[0]  n[1]  n[2]
        ┌─────┬─────┬─────┐
  n[0]  │ n0² │n0*n1│n0*n2│
        ├─────┼─────┼─────┤
  n[1]  │n1*n0│ n1² │n1*n2│
        ├─────┼─────┼─────┤
  n[2]  │n2*n0│n2*n1│ n2² │
        └─────┴─────┴─────┘
```

This gives `||row_i|| * ||row_j||` for every pair — exactly the denominator.

Key: use `np.linalg.norm(X, axis=1)` to get per-row norms (not the whole-matrix norm).

## Handling Zero Vectors

When a row is all zeros, its norm is 0, causing division by zero → `nan`.

Two approaches:
1. **`np.nan_to_num(result)`** — replace nan/inf with 0 after dividing (works but produces a RuntimeWarning)
2. **Replace zero denominators before dividing** — cleaner, no warning:
   ```python
   denominator[denominator == 0] = 1  # 0/1 = 0.0, correct result
   ```

## Final Solution

```python
def cosine_similarity_matrix(X: np.ndarray) -> np.ndarray:
    numerator = X @ X.T
    norms = np.linalg.norm(X, axis=1)
    denominator = np.outer(norms, norms)
    denominator[denominator == 0] = 1
    return numerator / denominator
```
