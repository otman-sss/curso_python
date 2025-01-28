# Archivo con todas las funciones necesarias para la aplicacion "linea"
import matplotlib.pyplot as plt
def calcular_y(x:float, m:float, b:float)-> float:
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: interseccion en y
    '''

    return (m*x) + b
def grafica_linea(X:list, Y:list, m:float, b:float):
    '''
    Grafica una linea recta
    X: lista de valores de x
    Y: lista de valores de Y
    Regresa: nada
    '''
    plt.plot(X,Y)
    plt.title(f'Linea con pendiente {m} y ordenada al origen {b}')
    plt.xlabel('Y')
    plt.ylabel('X')
    plt.show()

def test_linea():
    '''
    Prueba de funcionamiento de calcular_Y
    '''

    y = calcular_y(0.0, 2.0, 3.0)
    return y

if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Test exitoso')
    else:
        print('Test fallido')    
