import matplotlib.pyplot as plt
import seaborn as sns

#plot position vector
def plot_position(U, title): 
    sns.set()
    plt.figure()
    plt.plot(U[0,:], U[1,:])
    plt.title(title)
    plt.xlabel('Rx [m]')
    plt.ylabel('Ry [m]')

#subplot all position vectors
def plot_positions(UU, names, dt): 
    sns.set()
    a = 2
    b = 2
    z = 0
    fig, axs = plt.subplots(a, b)
    fig.suptitle("Orbits Position, $\Delta t$ = " + str(dt) + "[s]")
    fig.tight_layout(pad=0.8)

    for i in range(a):
        for y in range(b):
            axs[i, y].plot(UU[z,0], UU[z,1])
            axs[i, y].set_title(names[z])
            z = z + 1

    for ax in axs.flat:
        ax.set(xlabel='Rx [m]', ylabel='Ry [m]')


#plot specific energy (all same graphic)
def plot_energy(e, names, t, dt): 
    sns.set()
    plt.figure()
    for i in range(len(names)):
        plt.plot(t, e[i,:], label=names[i])

    plt.title("Specific Energy $\Delta t$ = " + str(dt) + "[s]")
    plt.xlabel('Time [s]')
    plt.ylabel('Energy')
    plt.legend()


#subplot all errors
def plot_error(Errors, names, t, dt): 
    sns.set()
    a = 2
    b = 2
    z = 0
    fig, axs = plt.subplots(a, b)
    fig.suptitle("Orbits Numerical Errors, $\Delta t$ = " + str(dt) + "[s]")
    fig.tight_layout(pad=0.8)

    for i in range(a):
        for y in range(b):
            axs[i, y].plot(t, Errors[z,0], label="Rx error")
            axs[i, y].plot(t, Errors[z,1], label="Ry error")
            axs[i, y].plot(t, Errors[z,4], label="|R|  error")
            axs[i, y].set_title(names[z])
            z = z + 1

    for ax in axs.flat:
        ax.set(xlabel='Time [s]', ylabel='R error [m]')
        ax.legend()

#plot errors position modules
def plot_met_error(Errors, names, t, dt): 
    sns.set()
    plt.figure()
    for i in range(len(names)):
        plt.plot(t, Errors[i,4], label=names[i])

    plt.title("Numerical Errors comparison, $\Delta t$ = " + str(dt) + "[s]")
    plt.xlabel('Time [s]')
    plt.ylabel('Error [m]')
    plt.legend()


#subplot all convergence rates
def plot_conv_rate(Conv_rate, names, dt):
    sns.set()
    a = 2
    b = 2
    z = 0
    fig, axs = plt.subplots(a, b)
    fig.suptitle("Convergence Rate, $\Delta t$ = " + str(dt) + "[s]")
    fig.tight_layout(pad=0.8)

    for i in range(a):
        for y in range(b):
            axs[i, y].plot(Conv_rate[z,0], Conv_rate[z,1])
            axs[i, y].set_title(names[z])
            z = z + 1

    for ax in axs.flat:
        ax.set(xlabel='log(N)', ylabel='log(E)')

#comparison convergence rate
def plot_comparision_cr(Conv_rate, names, dt): 
    sns.set()
    plt.figure()
    for i in range(len(names)):
        cr = Conv_rate[i,:]
        plt.plot(cr[0,:], cr[1,:], label=names[i])

    plt.title("Convergence Rate comparison, $\Delta t$ = " + str(dt) + "[s]")
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.legend()
