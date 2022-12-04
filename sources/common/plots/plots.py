import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np

#plot position vector
def plot_position(U, title): 
    sns.set()
    plt.figure()
    plt.plot(U[0,:], U[1,:])
    plt.title(title)
    plt.xlabel('Rx [m]')
    plt.ylabel('Ry [m]')


def plot_aux1(subplo, rx, ry, nam):
    ax = plt.subplot(subplo)
    ax.plot(rx, ry)

    ax.set_title(nam)
    ax.set(xlabel='Rx [m]', ylabel='Ry [m]')


def plot_aux2(subplo, t, ex, ey, e, nam):
    ax = plt.subplot(subplo)
    ax.plot(t, ex, label="Rx error")
    ax.plot(t, ey, label="Ry error")
    ax.plot(t, e, label="|R| error")

    ax.set_title(nam)
    ax.set(xlabel='Time [s]', ylabel='Error [m]')
    ax.legend(loc='upper left')


def plot_aux3(subplo, log_n, log_e, nam):
    ax = plt.subplot(subplo)
    ax.plot(log_n, log_e, '--o')

    ax.set_title(nam)
    ax.set(xlabel='log(N)', ylabel='log(E)')


def plot_aux4(subplo, t, U, nam):
    ax = plt.subplot(subplo)
    ax.plot(t, U[0,:], 'b', label="Position")
    ax.plot(t, U[1,:], 'g', label="Velocity")

    ax.set_title(nam)
    ax.set(xlabel='Time [s]', ylabel='Position [m] / Velocity [m/s]')
    ax.legend()


#subplot all position vectors
def plot_positions(UU, mets, dt): 
    sns.set()

    if len(mets) % 2 == 0: #par
        b = int(len(mets)/2)
    else:                   #impar
        b = int(len(mets)/2) + 1
    
    if len(mets) >= 2:
        a = 2
    else:
        a = 1

    gs = gridspec.GridSpec(a, b)
    plt.figure()
    plt.suptitle("Orbits Position, $\Delta t$ = " + str(dt) + "[s]")
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.3, wspace=0.3, top=0.9, bottom=0.05, left=0.05, right=0.95)
    z = 0

    for i in range(b):
        if ((len(mets)%2 != 0) and (i >= b-1)): #odd and last column
            plot_aux1(gs[0, i], UU[z,0], UU[z,1], mets[z].__name__)
        else:
            for j in range(a):
                plot_aux1(gs[j, i], UU[z,0], UU[z,1], mets[z].__name__)
                z = z + 1

    #plt.savefig('doc/milestone4_latex/FIGURES/dt'+str(dt)+'_position.png', dpi=200)


#plot specific energy (all same graphic)
def plot_energy(e, mets, t, dt): 
    sns.set()
    plt.figure()
    for i in range(len(mets)):
        plt.plot(t, e[i,:], label=mets[i].__name__)

    plt.title("Specific Energy $\Delta t$ = " + str(dt) + "[s]")
    plt.xlabel('Time [s]')
    plt.ylabel('Energy')
    plt.legend()
    #plt.savefig('doc/milestone3_latex/FIGURES/dt'+str(dt)+'_energy.png', dpi=200)


#subplot all errors
def plot_error(Errors, mets, t, dt): 
    sns.set()

    if len(mets) % 2 == 0: #par
        b = int(len(mets)/2)
    else:                   #impar
        b = int(len(mets)/2) + 1

    if len(mets) >= 2:
        a = 2
    else:
        a = 1

    gs = gridspec.GridSpec(a, b)
    plt.figure()
    plt.suptitle("Orbits Numerical Errors, $\Delta t$ = " + str(dt) + "[s]")
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.3, wspace=0.3, top=0.9, bottom=0.05, left=0.05, right=0.95)
    z = 0

    for i in range(b):
        if ((len(mets)%2 != 0) and (i >= b-1)): #odd and last column
            plot_aux2(gs[0, i], t, Errors[z,0], Errors[z,1], Errors[z,len(Errors[0,:])-1], mets[z].__name__)
        else:
            for j in range(a):
                plot_aux2(gs[j, i], t, Errors[z,0], Errors[z,1], Errors[z,len(Errors[0,:])-1], mets[z].__name__)
                z = z + 1
            

#plot errors position modules
def plot_met_error(Errors, mets, t, dt): 
    sns.set()
    plt.figure()
    for i in range(len(mets)):
        plt.plot(t, Errors[i,len(Errors[0,:])-1], label=mets[i].__name__)

    plt.title("Numerical Errors comparison, $\Delta t$ = " + str(dt) + "[s]")
    plt.xlabel('Time [s]')
    plt.ylabel('Error [m]')
    plt.legend()
    #plt.savefig('doc/milestone3_latex/FIGURES/dt'+str(dt)+'_error_comparison.png', dpi=200)


def plot_conv_rate(Conv_rate, mets, dt):
    sns.set()

    if len(mets) % 2 == 0: #par
        b = int(len(mets)/2)
    else:                   #impar
        b = int(len(mets)/2) + 1

    if len(mets) >= 2:
        a = 2
    else:
        a = 1

    gs = gridspec.GridSpec(a, b)
    plt.figure()
    plt.suptitle("Convergence Rate, $\Delta t$ = " + str(dt) + "[s]")
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.3, wspace=0.3, top=0.9, bottom=0.05, left=0.05, right=0.95)
    z = 0

    for i in range(b):
        if ((len(mets)%2 != 0) and (i >= b-1)): #odd and last column
            plot_aux3(gs[0, i], Conv_rate[z,0], Conv_rate[z,1], mets[z].__name__)
        else:
            for j in range(a):
                plot_aux3(gs[j, i], Conv_rate[z,0], Conv_rate[z,1], mets[z].__name__)
                z = z + 1


#comparison convergence rate
def plot_comparision_cr(Conv_rate, mets, dt): 
    sns.set()
    plt.figure()
    for i in range(len(mets)):
        cr = Conv_rate[i,:]
        plt.plot(cr[0,:], cr[1,:], '--o', markersize=10, label=mets[i].__name__)

    plt.title("Convergence Rate comparison, $\Delta t$ = " + str(dt) + "[s]")
    plt.xlabel('log(N)')
    plt.ylabel('log(E)')
    plt.legend()
    #plt.savefig('doc/milestone3_latex/FIGURES/dt'+str(dt)+'_convergence_comparison.png', dpi=200)


#plot pos/vel oscillator
def plot_oscillator(U, t, dt, name):
    sns.set()
    plt.figure()
    plt.plot(t, U[0,:], 'b', label="Position")
    plt.plot(t, U[1,:], 'g', label="Velocity")

    plt.title("Oscillator, $\Delta t$ = " + str(dt) + "[s]. " + name)
    plt.xlabel('Time [s]')
    plt.ylabel('Position [m] / Velocity [m/s]')
    plt.legend()
    

#subplot all oscillators
def subplot_oscillators(UU, t, mets, dt):
    sns.set()

    if len(mets) % 2 == 0: #par
        b = int(len(mets)/2)
    else:                   #impar
        b = int(len(mets)/2) + 1

    if len(mets) >= 2:
        a = 2
    else:
        a = 1

    gs = gridspec.GridSpec(a, b)
    plt.figure()
    plt.suptitle("Oscillator, $\Delta t$ = " + str(dt) + "[s]")
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.3, wspace=0.3, top=0.9, bottom=0.05, left=0.05, right=0.95)
    z = 0

    for i in range(b):
        if ((len(mets)%2 != 0) and (i >= b-1)): #odd and last column
            plot_aux4(gs[0, i], t, UU[z,:], mets[z].__name__)
        else:
            for j in range(a):
                plot_aux4(gs[j, i], t, UU[z,:], mets[z].__name__)
                z = z + 1


#plot oscillator in all Dt
def plot_osc_dt(UU, TT, Dt, mets):
    sns.set()
    for z in range(len(mets)):
        plt.figure()
        plt.tight_layout()
        plt.subplots_adjust(hspace=0.3, wspace=0.3, top=0.95, bottom=0.05, left=0.05, right=0.95)
        gs = gridspec.GridSpec(2, 1)
        ax1 = plt.subplot(gs[0, 0])
        ax2 = plt.subplot(gs[1, 0])

        for i in range(len(Dt)):
            ax1.plot(TT[i], UU[i][z,0], label="$\Delta t$ = " + str(Dt[i]) + "[s]")
            ax2.plot(TT[i], UU[i][z,1], label="$\Delta t$ = " + str(Dt[i]) + "[s]")

        ax1.set_title("Oscillator Position, " + mets[z].__name__)     
        ax2.set_title("Oscillator Velocity, " + mets[z].__name__)
        ax1.set(xlabel='Time [s]', ylabel='Position [m]')
        ax2.set(xlabel='Time [s]', ylabel='Velocity [m/s]')
        ax1.set_xlim([TT[0][0], TT[0][-1]])
        ax2.set_xlim([TT[0][0], TT[0][-1]])
        ax1.legend()
        ax2.legend()


#plot stability
def plot_stability(x, y, rho, name):
    sns.set()
    plt.figure()
    plt.contour(x, y, np.transpose(rho), np.linspace(0, 1, 11))
    plt.title("Absolute Stability Region for " + name)
    plt.xlabel('Re')
    plt.ylabel('Imag')
    plt.axis('equal')
