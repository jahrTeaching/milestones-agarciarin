from common.constant import MU_em
import numpy as np
from scipy.optimize import newton, fsolve


#restricted 3 body problem
def rest_3b(U, t):
    mu = MU_em
    r = U[0:3]
    v = U[3:6]

    d_ = np.sqrt( (r[0]+mu)**2 + r[1]**2 + r[2]**2 )
    r_ = np.sqrt( (r[0]-1+mu)**2 + r[1]**2 + r[2]**2)

    dvx_dt = r[0] + 2 * v[1] - (1-mu) * ( r[0] + mu )/d_**3 - mu*(r[0]-1+mu)/r_**3
    dvy_dt = r[1] - 2 * v[0] - (1-mu) * r[1]/d_**3 - mu * r[1]/r_**3
    dvz_dt = - (1-mu)*r[2]/d_**3 - mu*r[2]/r_**3

    return np.array([v[0], v[1], v[2], dvx_dt, dvy_dt, dvz_dt])


#Lagrange points
def lagr_points(U0, Nl, Nc):
    Lp = np.zeros([Nl, Nc])

    def f(y):
        x = np.zeros(6)
        x[0:3] = y
        x[3:6] = 0
        fx = rest_3b(x, 0)
        return fx[3:6]
   
    for i in range(Nl):
        Lp[i,:] = fsolve(f, U0[i, 0:3])

    return Lp


#Lagrange points stability
def sist_matrix(U0, t, f):
    eps = 1e-6
    N = len(U0)
    A = np.empty([N, N])

    for i in range(N):
        delta = np.zeros(N)
        delta[i] = eps

        A[:,i] = (f(U0+delta, t) - f(U0-delta, t)) / (2*eps)

    return A

def lagr_points_stab(U0):
    def f(y, t):
        return rest_3b(y, 0)

    A = sist_matrix(U0, 0, f)
    
    return np.linalg.eig(A)
