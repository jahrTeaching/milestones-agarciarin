import scipy.optimize as scipyop

#Euler
def ExplicitEuler(U, dt, t, f):
    return U + dt*f(U, t)

#RK4
def RungeKutta4(U, dt, t, f):
    k1 = f(U, t)
    k2 = f(U+dt*k1/2, t)
    k3 = f(U+dt*k2/2, t)
    k4 = f(U+dt*k3, t)
    return U + dt*(k1 + 2*k2 + 2*k3 + k4)/6

#Inverse Euler
def InverseEuler(U, dt, t, F): 
    def Residual(X): 
        return X - U - dt * F(X, t)

    uu = scipyop.newton(func = Residual, x0 = U, tol = 10e-3) #tol: error of the zero value (necesarry if not RuntimeError)
    return uu

#Crank-Nicolson
def CrankNicolson(U, dt, t, F): 
    def Residual_CN(X):        
         return  X - a - dt/2 *  F(X, t + dt)

    a = U  +  dt/2 * F(U, t)  
    uu = scipyop.newton(Residual_CN, U)
    return uu