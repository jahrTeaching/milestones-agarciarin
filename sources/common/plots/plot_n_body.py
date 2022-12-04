import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#3D plot position
def plot_3D(U, t, Dt, m, Nb, Nc): #(Values, time, Delta t, method, Nbodies, Ncoord)
    sns.set()
    plt.figure(figsize=(10,9))
    ax = plt.axes(projection='3d')
    col = ['c', 'r', 'g', 'y']

    for i in range(Nb):
        a = 2*Nc*i
        ax.plot3D(U[a,:], U[a+2,:], U[a+4,:], label='Body ' + str(i+1), color=col[i])
        ax.plot(U[a,len(t)-1], U[a+2,len(t)-1], U[a+4,len(t)-1], color=col[i], marker='o', markersize=8)

    ax.set_title('Positions in 3D, ' + m.__name__ + ' method')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.legend()


def plot_vel(U, t, Dt, m, Nb, Nc):
    sns.set()
    plt.figure()

    for i in range(Nb):
        a = 2*Nc*i
        v = [U[a+1,:], U[a+3,:], U[a+5,:]]
        uu = np.empty(len(t))

        for k in range(len(t)):
            uu[k] = np.linalg.norm([v[0][k], v[1][k], v[2][k]])

        plt.plot(t, uu, label='Body ' + str(i+1))
    
    plt.title('Velocity modules, ' + m.__name__ + ' method')
    plt.xlabel('Time [s]')
    plt.ylabel('Velocity [m/s]')
    plt.legend()
