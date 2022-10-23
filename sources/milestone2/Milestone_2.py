#main
import matplotlib.pyplot as plt
import numpy as np

import CauchyProblem as cp
import Functions as fun
import Methods as met
import Orbits as orb

def main():

    #Initiate values
    print("Introduzca dt = ")
    dt = float(input())
    #dt = 0.01       #[s] 
    tf = 30.        #[s]

    R0 = 1.         #[m]
    V0 = 1.         #[m/s]
    Zeta0 = 0.      #[deg]

    N = int(tf/dt)+1    #Nº steps
    t = np.linspace(0, tf, N)
    U0 = fun.InitStateVector(R0, V0, Zeta0)

    #Cauchy solver orbits
    U_Euler = cp.CauchyProblem(U0, t, orb.Orbits, met.ExplicitEuler)
    U_RK4 = cp.CauchyProblem(U0, t, orb.Orbits, met.RungeKutta4)
    U_InvEuler = cp.CauchyProblem(U0, t, orb.Orbits, met.InverseEuler)
    U_CN = cp.CauchyProblem(U0, t, orb.Orbits, met.CrankNicolson)
    UU = np.array([U_Euler, U_RK4, U_InvEuler, U_CN])

    #Energy orbit
    E_Euler = orb.OrbitEnergy(U_Euler, t)
    E_RK4 = orb.OrbitEnergy(U_RK4, t)
    E_InvEuler = orb.OrbitEnergy(U_InvEuler, t)
    E_CN = orb.OrbitEnergy(U_CN, t)
    E = np.array([E_Euler, E_RK4, E_InvEuler, E_CN])

    Met_names = np.array(["Euler", "RK4", "Inverse Euler", "CN"])

    #Graphics
    fun.plot_Positions(UU, Met_names, dt)
    fun.plot_energy(E, Met_names, t)
    plt.show()

if __name__ == "__main__":
    main()
    