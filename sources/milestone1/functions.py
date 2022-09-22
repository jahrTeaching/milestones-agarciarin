#functions
import numpy as np
import math
import matplotlib.pyplot as plt

def InitStateVector(r, v, zeta, t):
    rx = r*math.cos(zeta)
    ry = r*math.sin(zeta)
    vx = -v*math.sin(zeta)
    vy = v*math.cos(zeta)
    return [rx, ry, vx, vy, t]

#Orbit
def Orbits(X):
    rx = X[0]
    ry = X[1]
    vx = X[2]
    vy = X[3]
    return [vx, vy, -rx/(rx**2+ry**2)**(3/2), -ry/(rx**2+ry**2)**(3/2)]

#Euler
def ExplicitEuler(X, dt, N):
    for i in range(0, N-1):
        X[0,i+1] = X[0,i] + dt*Orbits(X[:,i])[0]
        X[1,i+1] = X[1,i] + dt*Orbits(X[:,i])[1]
        X[2,i+1] = X[2,i] + dt*Orbits(X[:,i])[2]
        X[3,i+1] = X[3,i] + dt*Orbits(X[:,i])[3]
        X[4,i+1] = X[4,i] + dt
    return X
   
#Velocity modulus
def v_modulus(X, N):
    V = np.zeros([1,N])
    for i in range(0, N):
        V[:,i] = (X[2,i]**2+X[3,i]**2)**(1/2)
    return V

#Graphics
def plot_Euler_Position(X):
    plt.figure(1)
    plt.plot(X[0,:], X[1,:])
    plt.xlabel('Rx [m]')
    plt.ylabel('Ry [m]')  

def plot_Euler_V_vs_T(X, N):
    V = v_modulus(X, N)
    plt.figure(2)
    plt.plot(X[4,:], V[0,:])
    plt.xlabel('Time [s]')
    plt.ylabel('Velocity (modulus) [m/s]') 