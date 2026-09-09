"""Example usage for Cholesky Decomposition Skill."""
from client import CholeskyDecomposition

def main():
    print("Executing Cholesky Decomposition...")
    A = [[4.0, 12.0, -16.0], [12.0, 37.0, -43.0], [-16.0, -43.0, 98.0]]
    L = CholeskyDecomposition.factorize(A)
    print("Lower Triangular Cholesky Factor L:", L)

    # Verify A = L * L^T
    LLT = [[sum(L[i][k] * L[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            assert abs(A[i][j] - LLT[i][j]) < 1e-3
    print("Cholesky Decomposition verified successfully!")

if __name__ == "__main__":
    main()
