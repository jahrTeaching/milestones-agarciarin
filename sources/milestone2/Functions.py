#functions inistiate state vector and plots
import math
import numpy as np
import matplotlib.pyplot as plt

#Initiate Vector
def InitStateVector(r, v, zeta):
    zetaRad = math.radians(zeta)
    rx = r*math.cos(zetaRad)
    ry = r*math.sin(zetaRad)
    vx = -v*math.sin(zetaRad)
    vy = v*math.cos(zetaRad)
    return np.array([rx, ry, vx, vy])

#Graphics
def plot_Position(U, title): #plot position vector
    plt.figure()
    plt.plot(U[0,:], U[1,:])
    plt.title(title)
    plt.xlabel('Rx [m]')
    plt.ylabel('Ry [m]')

def plot_Positions(UU, names, dt): #subplot all position vectors
    a = 2
    b = 2
    z = 0
    fig, axs = plt.subplots(a, b)
    fig.suptitle("Orbits Position, dt = " + str(dt) + "[s]")
    fig.tight_layout(pad=1.5)

    for i in range(a):
        for y in range(b):
            axs[i, y].plot(UU[z,0], UU[z,1])
            axs[i, y].set_title(names[z])
            z = z + 1

    for ax in axs.flat:
        ax.set(xlabel='Rx [m]', ylabel='Ry [m]')

def plot_energy(e, names, t): #plot specific energy (same graphic)
    plt.figure()
    for i in range(len(names)):
        plt.plot(t, e[i,:], label=names[i])

    plt.title("Specific Energy")
    plt.xlabel('Time [s]')
    plt.ylabel('Energy')
    plt.legend()