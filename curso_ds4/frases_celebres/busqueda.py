import os
import csv
import argparse
import Levenshtein

# Funcion para leer el archivo CSV y devolver una lista de frases

def leer_csv(archivo):
    '''Lee un archivo CSV y devuelve una lista de frases'''
    frases = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append(fila[0])
    return frases

#Funcion para buscar palabras en las frases
def buscar_palabras(frases, palabras):
    '''Busca en una lista de palabras en una lista de frases'''        
    frases_encontradas = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                frases_encontradas.append(frase)
                break
    return frases_encontradas

# Funcion para mostrar las frases encontradas 
def mostrar_frases(frases):
    '''Muestra una lista de frases'''
    for frase in frases:
        print(frase)

# Funcion Principal
def main(archivo, lista_palabras):
    '''Funcion principal del programa'''
    #Leer el archivo CSV
    frases = leer_csv(archivo)
    #Buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, lista_palabras)

    mostrar_frases(frases_encontradas)

if __name__=='__main__':
    #Crear el parser
    parser = argparse.ArgumentParser(description= 'Buscar palabras en frases celebres de peliculas.')

    parser.add_argument('palabras', nargs = '+', help='Lista de palabras por buscar')
    #Obtener argumentos
    args = parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__), 'frases_consolidadas.csv')
    main("frases_consolidadas.csv", args.palabras)
    import levenshtein

input1 = "feria"
input2 = "fiera"
hamming = Levenshtein.distance(input1, input2)
print(f"La distancia Levenshtein entre {input1} y {input2} es : {hamming}")