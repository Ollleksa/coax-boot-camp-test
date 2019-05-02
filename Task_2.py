# Task_2
# What is the purpose of decorators?

import math as m


def rotate_coordinate_system(theta):
    '''
    Decorators is used for modification of other functions.
    In this example we had functions that work in some 2D cartesian coordinate system (XY).
    But then our coordinate system was rotated on angle Theta and become (X'Y'),
    but input and output must still be in the first system. In this case
    we can use decorator to make old functions for new purpose.
    https://en.wikipedia.org/wiki/Rotation_matrix

    If func() is linear operator U, then decorator change it to new coordinates by mathematical rules: U' = R*U*R^(-1)
    '''

    def decorator(func):
        def wrapper(x, y):
            # Before calling the function - rotate input (from XY to X'Y')
            x_rotated = x * m.cos(theta) - y * m.sin(theta)
            y_rotated = x * m.sin(theta) + y * m.cos(theta)
            # Call function and receive output (in X'Y')
            out_x_rotated, out_y_rotated = func(x_rotated, y_rotated)
            # Rotate result back to XY
            out_x = out_x_rotated * m.cos(theta) + out_y_rotated * m.sin(theta)
            out_y = -out_x_rotated * m.sin(theta) + out_y_rotated * m.cos(theta)
            return out_x, out_y

        return wrapper

    return decorator

def x_inversion(x, y):
    return -x, y

@rotate_coordinate_system(theta=m.pi/4)
def x_inversion_dec(x, y):
    return -x, y


def y_inversion(x, y):
    return x, -y

@rotate_coordinate_system(theta=m.pi/4)
def y_inversion_dec(x, y):
    return x, -y


def test():
    x, y = (1, 1)
    print('Starting points: ({}, {})'.format(x, y))
    print('Inverted by X: {}'.format(x_inversion(x, y)))
    print('Inverted by Y: {}'.format(y_inversion(x, y)))

    print('Inverted by X in new coordinates: {}'.format(x_inversion_dec(x, y)))
    print('Inverted by Y in new coordinates: {}'.format(y_inversion_dec(x, y)))


if __name__ == '__main__':
    print(rotate_coordinate_system.__doc__)
    test()