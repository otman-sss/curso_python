import tablero

def main():
    
     X = {"G":0, "P":0, "E":0}
     O = {"G":0, "P":0, "E":0}
     score = {"X":X,"O":O}
     numeros = [str(x) for x in range(1,10)]
     g = tablero.juego(dsimbolos)
     
     corriendo = True
     while corriendo:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score,g)
        tablero.despliega_tablero(score)
        seguir = input('Quieres seguir jugando? (s/n)' )
        if seguir.lower() == 'n':
            corriendo = False

if __name__ == '__main__':
    main()         