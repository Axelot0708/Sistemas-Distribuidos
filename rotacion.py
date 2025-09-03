import numpy as np

def rotarX(x, y, z, theta):
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R @ np.array([x, y, z])


def rotarY(x, y, z, theta):
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ np.array([x, y, z])


def rotarZ(x, y, z, theta):
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ np.array([x, y, z])


def rotar(x, y, z, theta, axis):
    if axis == 'x':
        return rotarX(x, y, z, theta)
    elif axis == 'y':
        return rotarY(x, y, z, theta)
    elif axis == 'z':
        return rotarZ(x, y, z, theta)

X = int(input("X: "))
Y = int(input("Y: "))
Z = int(input("Z: "))
grados = float(input("Grados: "))
eje = input("Eje(x, y, z): ")
thet = np.radians(grados)

vecRotado = rotar(X, Y, Z, thet, eje.lower())
print("Vector rotado:", vecRotado)