#functions
import numpy as np
import math
import matplotlib.pyplot as plt

def InitStateVector(r, v, zeta):
    zetaRad = math.radians(zeta)
    rx = r*math.cos(zetaRad)
    ry = r*math.sin(zetaRad)
    vx = -v*math.sin(zetaRad)
    vy = v*math.cos(zetaRad)
    return [rx, ry, vx, vy]

#Orbit
def Orbits(X):
    d = (X[0]**2 + X[1]**2)**1.5
    rx = -X[0]/d
    ry = -X[1]/d
    dxdt = X[2]
    dydt = X[3]
    return np.array([dxdt, dydt, rx, ry])

#Cauchy
def CauchyProblem(X0, t, f, method):
    X = np.array(np.zeros([len(X0), len(t)]))
    X[:,0] = X0
    for i in range(len(t)-1):
        dt = t[i+1] - t[i]
        X[:,i+1] = method(X[:,i], dt, f)

    return X

#Euler
def ExplicitEuler(X, dt, f):
    return X + dt*f(X)

#RK4
def RungeKutta4(X, dt, f):
    k1 = f(X)
    k2 = f(X+dt*k1/2)
    k3 = f(X+dt*k2/2)
    k4 = f(X+dt*k3)
    return X + dt*(k1 + 2*k2 + 2*k3 + k4)/6

#Graphics
def plot_Position(X, n, title):
    plt.figure(n)
    plt.plot(X[0,:], X[1,:])
    plt.title(title)
    plt.xlabel('Rx [m]')
    plt.ylabel('Ry [m]')  