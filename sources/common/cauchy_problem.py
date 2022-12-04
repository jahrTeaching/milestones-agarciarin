import numpy as np
from common.methods.methods import explicit_euler, leap_frog

def cauchy_problem(U0, t, f, method):
    U = np.array(np.zeros([len(U0), len(t)]))
    U[:,0] = np.transpose(U0)
    dt = t[1] - t[0]

    for i in range(len(t)-1):

        if method == leap_frog:
            if t[i]==0:
                U[:,i+1] = method(U[:,0], explicit_euler(U[:,0], dt, t[i], f), dt, t[i], f)
            else:
                U[:,i+1] = method(U[:,i-1], U[:,i], dt, t[i], f)    
        else:
            U[:,i+1] = method(U[:,i], dt, t[i], f)
        
    return U
