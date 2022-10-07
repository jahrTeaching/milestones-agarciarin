import numpy as np

def CauchyProblem(U0, t, f, method):
    U = np.array(np.zeros([len(U0), len(t)]))
    U[:,0] = np.transpose(U0)
    for i in range(len(t)-1):
        dt = t[i+1] - t[i]
        U[:,i+1] = method(U[:,i], dt, t, f)

    return U