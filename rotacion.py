import numpy as np

def rot_x(x, y, z, theta):
    '''
    Rota un vector alrededor del eje X.

    Parameters:
        x (float): coordenada en X
        y (float): coordenada en Y
        z (float): coordenada en Z
        theta (float): ángulo de rotación en radianes

    Returns:
        np.ndarray: vector rotado [x', y', z']
    '''
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R @ np.array([x, y, z])


def rot_y(x, y, z, theta):
    '''
    Rota un vector alrededor del eje Y.

    Parameters:
        x (float): coordenada en X
        y (float): coordenada en Y
        z (float): coordenada en Z
        theta (float): ángulo de rotación en radianes

    Returns:
        np.ndarray: vector rotado [x', y', z']
    '''
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ np.array([x, y, z])


def rot_z(x, y, z, theta):
    '''
    Rota un vector alrededor del eje Z.

    Parameters:
        x (float): coordenada en X
        y (float): coordenada en Y
        z (float): coordenada en Z
        theta (float): ángulo de rotación en radianes

    Returns:
        np.ndarray: vector rotado [x', y', z']
    '''
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ np.array([x, y, z])


def rotar(x, y, z, theta, axis):
    '''
    Rota un vector en 3D alrededor de un eje específico.

    Parameters:
        x (float): coordenada en X
        y (float): coordenada en Y
        z (float): coordenada en Z
        theta (float): ángulo de rotación en radianes
        axis (string): eje de rotación; puede ser 'x', 'y' o 'z'

    Returns:
        np.ndarray: vector rotado [x', y', z']
    '''
    if axis.lower() == 'x':
        return rot_x(x, y, z, theta)
    elif axis.lower() == 'y':
        return rot_y(x, y, z, theta)
    elif axis.lower() == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'")


# Programa principal
X = int(input("X: "))
Y = int(input("Y: "))
Z = int(input("Z: "))
grados = float(input("Grados: "))
eje = input("Eje: ")

# Convertir a radianes
theta = np.radians(grados)

# Rotar
vec_rotado = rotar(X, Y, Z, theta, eje)
print("Vector rotado:", vec_rotado)
