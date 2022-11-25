import numpy as np
import common.cauchy_problem as cp


def richardson_error(U0, t, f, method, q): #(U0, time, function, method, order)
    N = len(t)
    E = np.zeros([len(U0), N])
    e_pos = np.array(np.zeros([1, N])) #error position module

    t1 = t
    t2 = np.linspace(0, t[N-1], 2*N)

    U1 = cp.cauchy_problem(U0, t1, f, method)
    U2 = cp.cauchy_problem(U0, t2, f, method)
    
    for i in range(N):
        E[:, i] = (U2[:,2*i] - U1[:,i]) / (1-1/(2**q)) 
        e_pos[0, i] = (E[0, i]**2 + E[1, i]**2)**0.5
    
    E = np.insert(E, len(U0), e_pos, axis=0)

    return E
