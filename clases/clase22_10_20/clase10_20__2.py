import numpy as np

def main():
    U = np.array([1, 2, 3, 4])
    U = np.reshape(U, (2,2))
    print("U=", U)

    """
    U[:, [0,1]] = U[:, [1,0]]
    print("U = ", U)
    """

    (U[:, 0], U[:, 1])  = (U[:, 1].copy(), U[:, 0].copy())
    print("U = ", U)


if __name__ == "__main__":
    main()