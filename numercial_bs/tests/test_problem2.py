import numpy as np
import pytest
from src.problem2 import cosine_similarity_matrix


class TestCosineSimilarity:
    def test_identical_vectors(self):
        X = np.array([[1.0, 0.0], [1.0, 0.0]])
        result = cosine_similarity_matrix(X)
        expected = np.array([[1.0, 1.0], [1.0, 1.0]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_orthogonal_vectors(self):
        X = np.array([[1.0, 0.0], [0.0, 1.0]])
        result = cosine_similarity_matrix(X)
        expected = np.array([[1.0, 0.0], [0.0, 1.0]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_opposite_vectors(self):
        X = np.array([[1.0, 0.0], [-1.0, 0.0]])
        result = cosine_similarity_matrix(X)
        expected = np.array([[1.0, -1.0], [-1.0, 1.0]])
        np.testing.assert_array_almost_equal(result, expected)

    def test_diagonal_is_one(self):
        X = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        result = cosine_similarity_matrix(X)
        np.testing.assert_array_almost_equal(np.diag(result), [1.0, 1.0, 1.0])

    def test_symmetry(self):
        X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        result = cosine_similarity_matrix(X)
        np.testing.assert_array_almost_equal(result, result.T)

    def test_shape(self):
        X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        result = cosine_similarity_matrix(X)
        assert result.shape == (4, 4)

    def test_known_values(self):
        X = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]])
        result = cosine_similarity_matrix(X)
        # cos_sim([1,0,0], [1,1,0]) = 1/sqrt(2)
        np.testing.assert_almost_equal(result[0, 2], 1.0 / np.sqrt(2))
        np.testing.assert_almost_equal(result[1, 2], 1.0 / np.sqrt(2))
        np.testing.assert_almost_equal(result[0, 1], 0.0)

    def test_zero_vector_handling(self):
        X = np.array([[1.0, 2.0], [0.0, 0.0], [3.0, 4.0]])
        result = cosine_similarity_matrix(X)
        # Zero vector should have 0 similarity with everything
        np.testing.assert_almost_equal(result[1, 0], 0.0)
        np.testing.assert_almost_equal(result[1, 2], 0.0)
        np.testing.assert_almost_equal(result[0, 1], 0.0)
        np.testing.assert_almost_equal(result[1, 1], 0.0)

    def test_single_vector(self):
        X = np.array([[3.0, 4.0]])
        result = cosine_similarity_matrix(X)
        np.testing.assert_array_almost_equal(result, [[1.0]])
