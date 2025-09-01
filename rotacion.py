import numpy as np

def rot_x(x, y, z, theta):
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R @ np.array([x, y, z])


def rot_y(x, y, z, theta):
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ np.array([x, y, z])


def rot_z(x, y, z, theta):
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ np.array([x, y, z])


def rotar(x, y, z, theta, axis):
    if axis.lower() == 'x':
        return rot_x(x, y, z, theta)
    elif axis.lower() == 'y':
        return rot_y(x, y, z, theta)
    elif axis.lower() == 'z':
        return rot_z(x, y, z, theta)

X = int(input("X: "))
Y = int(input("Y: "))
Z = int(input("Z: "))
grados = float(input("Grados: "))
eje = input("Eje(x, y, z): ")
theta = np.radians(grados)

vec_rotado = rotar(X, Y, Z, theta, eje.lower())
print("Vector rotado:", vec_rotado)
