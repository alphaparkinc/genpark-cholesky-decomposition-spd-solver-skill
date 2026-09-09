"""
Autonomous Agent Cholesky Decomposition Skill
Pure Python Standard Library implementation.
"""
import math
from typing import List, Dict, Any

class CholeskyDecomposition:
    """
    Cholesky LL^T decomposition for symmetric positive-definite matrices.
    """
    @staticmethod
    def factorize(A: List[List[float]]) -> List[List[float]]:
        n = len(A)
        L = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                s = sum(L[i][k] * L[j][k] for k in range(j))
                if i == j:
                    diff = A[i][i] - s
                    if diff < -1e-9:
                        raise ValueError("Matrix is not positive definite")
                    L[i][j] = math.sqrt(max(0.0, diff))
                else:
                    L[i][j] = (A[i][j] - s) / L[j][j] if L[j][j] > 1e-12 else 0.0
        return [[round(x, 6) for x in row] for row in L]
