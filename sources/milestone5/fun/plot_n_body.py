import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np


#3D plot position
def plot_3D(U, t, Dt, m, Nb, Nc): #(Values, time, Delta t, method, Nbodies, Ncoord)
    sns.set()
    plt.figure(figsize=(6,5))
    ax = plt.axes(projection='3d')

    for i in range(Nb):
        a = 2*Nc*i
        ax.plot3D(U[a,:], U[a+1,:], U[a+2,:], label='Body ' + str(i+1))

        ax.set_title('Positions in 3D, ' + m.__name__ + ' method')
        ax.set_xlabel('X [m]')
        ax.set_ylabel('Y [m]')
        ax.set_zlabel('Z [m]')
        ax.legend()













