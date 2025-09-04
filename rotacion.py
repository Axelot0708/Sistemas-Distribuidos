import numpy as np


def rot_x(x, y, z, theta):
    '''
    Rotar un vector en el eje X

    Parameters:
        x(float): valor de la coordenada X
        y(float): valor de la coordenada Y
        z(float): valor de la coordenada Z
        theta(float): el angulo de rotación del vector

    Returns:
        np.array([x, y, z]): devuelve el vector rotado en el angulo de theta en el eje X
    '''
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])
    return R @ np.array([x, y, z])

def rot_y(x, y, z, theta):
    '''
    Rotar un vector en el eje Y

    Parameters:
        x(float): valor de la coordenada X
        y(float): valor de la coordenada Y
        z(float): valor de la coordenada Z
        theta(float): el angulo de rotación del vector

    Returns:
        np.array([x, y, z]): devuelve el vector rotado en el angulo de theta en el eje Y
    '''
    R = np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return R @ np.array([x, y, z])

def rot_z(x, y, z, theta):
    '''
    Rotar un vector en el eje Z

    Parameters:
        x(float): valor de la coordenada X
        y(float): valor de la coordenada Y
        z(float): valor de la coordenada Z
        theta(float): el angulo de rotación del vector

    Returns:
        np.array([x, y, z]): devuelve el vector rotado en el angulo de theta en el eje Z
    '''
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])
    return R @ np.array([x, y, z])


def rotar(x, y, z, theta, axis):
    '''
    Rota un vector en un eje especifico

    Parameters:
        x (float): valor de la coordenada X
        y (float): valor de la coordenada Y
        z (float): valor de la coordenada Z
        theta(float): el angulo de rotación del vector
        axis(str): especifica el eje que se quiere rotar y se convierte a minúscula para que concuerden

    Returns:
        np.array([x, y, z]): devuelve el vector rotado en el eje especificado en el angulo theta
    '''
    axis = axis.lower()
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)