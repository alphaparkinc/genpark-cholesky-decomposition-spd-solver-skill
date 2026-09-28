from client import CholeskyDecomposition

def main():
    A = [[4.0, 12.0, -16.0], [12.0, 37.0, -43.0], [-16.0, -43.0, 98.0]]
    L = CholeskyDecomposition.decompose(A)
    print("Cholesky Factor L:")
    for row in L:
        print(" ", [round(v, 2) for v in row])
    assert abs(L[0][0] - 2.0) < 1e-4

if __name__ == "__main__":
    main()
