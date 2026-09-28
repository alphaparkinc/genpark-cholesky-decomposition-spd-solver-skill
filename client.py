"""Cholesky Decomposition for Symmetric Positive-Definite (SPD) Matrices.
100% Python Standard Library.
"""

import math

class CholeskyDecomposition:
    """Computes lower-triangular Cholesky factor L such that A = L * L^T."""

    @staticmethod
    def decompose(A: list) -> list:
        n = len(A)
        L = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                s = sum(L[i][k] * L[j][k] for k in range(j))
                if i == j:
                    val = A[i][i] - s
                    if val <= 0:
                        raise ValueError("Matrix is not symmetric positive-definite")
                    L[i][j] = math.sqrt(val)
                else:
                    L[i][j] = (A[i][j] - s) / L[j][j]
        return L
