"""
Problem 2: Cosine Similarity Matrix (NumPy)
============================================
~10 minutes | NumPy only (no loops over rows)

Given a 2D numpy array X of shape (N, D) where each row is a D-dimensional vector,
compute the NxN pairwise cosine similarity matrix.

Cosine similarity between vectors u and v:
    cos_sim(u, v) = (u . v) / (||u|| * ||v||)

Implement:

1. cosine_similarity_matrix(X: np.ndarray) -> np.ndarray
   - X has shape (N, D)
   - Returns array of shape (N, N) where element [i, j] is cos_sim(X[i], X[j])
   - The diagonal should be 1.0 (a vector is perfectly similar to itself)
   - Handle the edge case: if a row is all zeros, its similarity with anything should be 0.0

Constraint: Must be VECTORIZED. No Python for-loops over rows.
           Use numpy operations (dot products, broadcasting, etc.)
"""

import numpy as np


def cosine_similarity_matrix(X: np.ndarray) -> np.ndarray: 
    numerator = np.matmul(X, X.T) # X@X.T
    norms = np.linalg.norm(X, axis=1)
    denomenator = np.outer(norms, norms)
    csm = numerator / denomenator
    return np.nan_to_num(csm)

# def _cosine_sim_two_vectors(u: np.ndarray, v: np.ndarray) -> float:
#     numerator = np.dot(a=u, b=v)
#     u_norm = np.linalg.norm(u)
#     v_norm = np.linalg.norm(u)
#     denomenator = u_norm * v_norm
#     if denomenator == 0.0:
#         return 0.0
#     return numerator / denomenator
