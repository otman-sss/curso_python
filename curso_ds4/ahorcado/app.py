
'''
Programa principal del juego del ahorcado
'''
import os
import string
import funciones as fn
from random import choice
import argparse

def main(archivo_texto:str, nombre_plantilla="plantilla"):
    '''
    Programa principal
    '''
    #Cargamos las plantillas
    plantillas = fn.carga_plantillas('plantilla')
    lista_oraciones= fn.carga_archivo_texto('./datos/pg15532.txt')
    palabras = fn.obten_palabras(lista_oraciones)
    o = 5 #OPORTUNIDADES
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('GANASTE!')
            break
    print(f"La palabra era: {p}") 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('archivo', help='Archivo de texto con palabras', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print('El archivo no existe')
        exit()
    #archivo = './datos/pg15532.txt' 
    main(archivo)       