import numpy as np

#punteros
"""
L = [1, 2, 3]
pL = L
L[0] = 0

print(pL)

print(id(L))
L = L + [1]
print(L)
print(id(L))
"""

"""
a = np.array([1, 2, 3])

pa = a
a[:] = a[:]+1 #alias
print(a)
print(pa)
print(id(a))
print(id(pa))
"""

a = np.array([1, 2, 3])
pa = np.reshape(a, (2,2))
print(pa)
