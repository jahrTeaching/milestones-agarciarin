import numpy as np
import common.cauchy_problem as cp


def convergence_rate(U0, t, f, method, m): #(U0, time, function, method, nº points)
    log_E = np.zeros(m)
    log_N = np.zeros(m)
    N = len(t)-1
    tf = t[N-1]

    t1 = t
    U1 = cp.cauchy_problem(U0, t1, f, method)

    for i in range(m):
        N = 2*N
        t2 = np.linspace(0, tf, N+1)
        U2 = cp.cauchy_problem(U0, t2, f, method)

        E = np.linalg.norm(U2[:,N] - U1[:,int(N/2)])
        log_E[i] = np.log10(E)
        log_N[i] = np.log10(N)

        t1 = t2
        U1 = U2

    return [log_N, log_E]
    