class Sport:
    '''
    Clase para representar un deporte
    '''
    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if isinstance(players, int): #Verificamos que players es un entero
            self.players = players
        else:
            self.players = int(players)    
        self.league = league     

    def __str__(self):
        return f"Sport: {self.name}, {self.players},{self.league}"    
    
    def __repr__(self) -> str:
        '''Represemtacion en string de Sport'''
        return f"Sport(name = '{self.name}', players = {self.players}, league = '{self.league}')"
    
    def to_json(self) -> dict:
        '''Convertir Sport a JSON'''
        return {"name": self.name, "players":self.players, "league":self.league}

if __name__ == '__main__':
    '''nfl = Sport("Football", 11, "NFL")
    print(nfl)
    print(repr(nfl))
    print(nfl.to_json())
    lmp = Sport("Baseball", 9, "LMP")
    print(lmp)
    print(repr(nfl))
    print(lmp.to_json())
    lmp = eval(repr(lmp))
    print(lmp2)'''
    s = Sport("Soccer",11,"FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    NFL = Sport("Football","11","NFL")
    LMP = Sport("Football",9,"LMP")
    MLB = Sport("Baseball",9,"MLB")
    LMX = Sport("Soccer",11,"Liga MX")
    NBA = Sport("Basketball",5,"NBA")
    lista_deportes = {NFL, LMP, MLB, LMX, NBA, s}
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")
    sports_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sports_list.append(d)
    print(sports_list)
    print(sports_list(0).to_json())
    #Escribiremos el archivo en formato JSON 
    import json
    archivo_json = "deportes.json"
    sports_json = [sport.to_json() for sport in sports_list]
    #Wirte the entire list as a single JSON array
    with open(archivo_json, "w") as file:
        json.dump(sports_json, file, indent = 4)

        #Leemos el archivo JSON 
        sport_list_json = []
        with open(archivo_json, "r") as file:
            sport_list_json = json.load(file)
        print(sport_list_json)    

