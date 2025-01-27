import funciones
def calcular_y(x, m, b):
    '''
    Calcula el valor de y en una linea recta
    x: el valor de x
    m: pendiente
    b: interseccion en y

    '''
    return m*x + b
def main():
    m=2
    b=3
    X= [x for x in range(1,11)]
    Y = [funciones.calcular_y(x,m,b) for x in X]
    print("Enteros:")
    coordenadas_enteros = list(zip(X,Y))
    print(coordenadas_enteros)
    XF = [x for x in range(1,11,0,5)]
    YF = [funciones.calcular_y(x,m,b) for x in XF]
    coordenadas_flotantes = list(zip(XF,YF))
    print("Flotantes:")
    print(coordenadas_flotantes)
    
if __name__ =='__main__':
    main()  