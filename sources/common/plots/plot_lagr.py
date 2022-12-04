import matplotlib.pyplot as plt
import seaborn as sns


#Plot Lagrange Points
def plot_lagr(Lps):
    E = [0, 0, 0]
    M = [1, 0, 0]

    sns.set()
    plt.figure(figsize=(10,9))
    ax = plt.axes(projection='3d')
    col = ['c', 'r', 'g', 'y', 'm']

    ax.plot(E[0], E[1], E[2], color='darkblue', marker='o', markersize=25, label='Earth')
    ax.plot(M[0], M[1], M[2], color='grey', marker='o', markersize=15, label='Moon')

    for i in range(len(Lps)):
        Lp = Lps[i]
        ax.plot(Lp[0], Lp[1], Lp[2], color=col[i], marker='o', markersize=6, label='L' + str(i+1))

    ax.set_title('Lagrange Points in 3D')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.set_zlim([-0.1, 0.1])
    ax.legend(loc='upper left')


#Plot perturbed orbit around lagrange point (INDIVIDUAL)
def plot_one_orb_lagr(Lp, U, n, m): #(LagrangePoint, Values, method)
    sns.set()
    plt.figure(figsize=(10,9))
    ax = plt.axes(projection='3d')
    ax.plot(Lp[0], Lp[1], Lp[2], marker='o', markersize=5, label='L' + str(n))
    ax.plot3D(U[0,:], U[1,:], U[2,:], label='Orbit')

    ax.set_title('Orbit around Lagrange Point L' + str(n) +' in 3D, ' + m.__name__ + ' method')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.set_zlim([-1, 1])
    ax.legend()


#Plot perturbed orbits around lagrange points
def plot_orb_lagr(Lps, UU, m): #(LagrangePoint, Values, method)
    E = [0, 0, 0]
    M = [1, 0, 0]
    sns.set()
    plt.figure(figsize=(10,9))
    ax = plt.axes(projection='3d')
    col = ['c', 'r', 'g', 'y', 'm']
    
    ax.plot(E[0], E[1], E[2], color='darkblue', marker='o', markersize=10, label='Earth')
    ax.plot(M[0], M[1], M[2], color='grey', marker='o', markersize=6, label='Moon')

    for i in range(len(Lps)):
        Lp = Lps[i]
        U = UU[i]
        ax.plot(Lp[0], Lp[1], Lp[2], color=col[i], marker='o', markersize=4)
        ax.plot3D(U[0,:], U[1,:], U[2,:], label='Orbit around L' + str(i+1), color=col[i])

    ax.set_title('Orbit around Lagrange Point in 3D, ' + m.__name__ + ' method')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.set_zlim([-1, 1])
    #ax.set_aspect('equal')
    ax.legend()


#Plot lagrange points stability
def plot_stab(val, n):
    sns.set()
    plt.figure()
  
    x = [ele.real for ele in val] # extract real part
    y = [ele.imag for ele in val] # extract imaginary part

    plt.scatter(x, y)
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')

    plt.title('Stability of Lagrange Point L' + str(n))
    plt.xlabel('Real')
    plt.ylabel('Imag')
