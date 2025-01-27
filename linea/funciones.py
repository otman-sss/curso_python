# Archivo con todas las funciones necesarias para la aplicacion "linea"
def calcular_y(x, m, b):
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: interseccion en y
    '''

    return (m*x) + b

def test_linea():
    '''
    Prueba de funcionamiento de calcular_Y
    '''

    y = calcular_y(0, 2, 3)
    return y

if __name__ == '__main__':
    if test_linea() == 3:
        print('Test exitoso')
    else:
        print('Test fallido')    
