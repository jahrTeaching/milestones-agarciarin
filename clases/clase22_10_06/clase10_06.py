import numpy as np

#funcion impura
counter = 0
def impure1(x):
    global counter

    counter = counter + 1

    return x + counter

def impure2(l):
    l += 5
    return l

def impure3(l):
    print(id(l))
    l = l + "su"
    print(id(l))
    return l

#recursivo
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

#
def f(x):
    return x**2

v = np.array([1,2,3])
w = f(v)

#
vv = np.array(list(map(f,v)))


#Salidas
print(impure1(10))
print(impure1(10))
print(impure2(10))
print(impure2(10))
print(impure3("hola"))
print(factorial(5))

print("w = ", w)
print("vv = ", vv)

