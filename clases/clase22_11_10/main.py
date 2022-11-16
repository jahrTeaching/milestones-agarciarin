




def main():
    A = [[1, 2], [3,4]]
    N, M = len(A), len(A[0])
    C = [[A[i][j] for i in range(N)] for j in range(M)]

    C[:][:] = A[:][:]
    A[1][1] = 0

    print("C", C)


if __name__ == "__main__":
    main()
