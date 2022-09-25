#main
import numpy as np
import functions as fun
import matplotlib.pyplot as plt

#const
R0 = 1.             #[m]
V0 = 1.             #[m/s]
Zeta0 = 0.          #[deg]
dt = 10**-2         #[s] 
tf = 10.            #[s]

N = int(tf/dt)+1    #Nº steps
t = np.linspace(0, tf, N)
X0 = fun.InitStateVector(R0, V0, Zeta0)

#Cauchy
X_Euler = fun.CauchyProblem(X0, t, fun.Orbits, fun.ExplicitEuler)
X_RK4 = fun.CauchyProblem(X0, t, fun.Orbits, fun.RungeKutta4)

#Graphics
fun.plot_Position(X_Euler, 1, "Explicit Euler")
fun.plot_Position(X_RK4, 2, "Runge-Kutta 4")
plt.show()