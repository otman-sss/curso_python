
'''
Funciones auxiliares del juego Ahorcado
'''
import unicodedata
import string
from random import choice

def carga_archivo_texto(archivo:str)-> list:
    '''
    Carga un archivo de text y devuelve una lista con oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla) -> dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''    
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del juego
    '''
    if nivel >= 0 and nivel <=5:
        template = diccionario[nivel]
        for renglon in template:
          print(renglon)

def obten_palabras(lista:list) -> list:
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    # Convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    #Removemos signos de puntuacion y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # Removemos numeros, perentesis, corchetes y otros caracteres 
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # Removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii','ignore').decode('ascii') for palabra in set_palabras}
    return list(set_palabras)

def adivina_letra(abc:str, palabra:str,letras_adivinadas:set,turnos:int) -> int:
    '''
    Adivina una letra de una palabra 
    '''
    palabra_oculta = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"    
    print(f'Tienes {turnos } turnos')
    abcd = ' '.join(abc.values())
    print(f'La palabra es: {palabra_oculta}')
    print(f'El abecedario es: {abcd}')
    letra = input('Ingresa una letra: ')
    if len(letra) != 1 or letra not in abc:
        print('Ingresa una letra valida')
    else:
        if letra in palabra:
            letras_adivinadas.add(letra)
            abc[letra] == "*"
        else:
            turnos -= 1
            abc[letra] = "*" 
    return turnos               

if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
    t = adivina_letra(abcdario, p, adivinadas, t)
    print(t)
