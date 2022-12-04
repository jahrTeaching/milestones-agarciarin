from numpy import zeros, float64, abs
from common.ode_methods.methods import leap_frog

def stability_regions(x, y, method):
    N = len(x)
    rho =  zeros((N, N),  dtype=float64)

    for i in range(N): 
        for j in range(N):
            w = complex(x[i], y[j])
            if method == leap_frog:
                r = method(1, 1, 1, 0, lambda u, t: w*u)
            else:
                r = method(1, 1, 0, lambda u, t: w*u)

            rho[i, j] = abs(r)

    return rho
