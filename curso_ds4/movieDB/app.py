from flask import Flask, request, url_for, render_template, redirect, flash
import os
import random
import movie_classes as mc


app = Flask(__name__)
app.secret_key = os.urandom(24) #Clave secreta para la sesion
sistema = mc.SistemaCine()
archivo_actores    = "datos/movies_db - actores.csv"
archivo_peliculas  = "datos/movies_db - peliculas.csv"
archivo_relaciones = "datos/movies_db - relacion.csv"
archivo_usuarios   = "datos/movies_db - users_hashed.csv"
relaciones_csv = "datos/movie_db - relacion.csv"
sistema.cargar_csv(archivo_actores, mc.Actor)
sistema.cargar_csv(archivo_peliculas, mc.Pelicula)
sistema.cargar_csv(archivo_relaciones, mc.Relacion)    
sistema.cargar_csv(archivo_usuarios, mc.User)

@app.route('/')
def index():
    '''Pagina principal de la aplicacion'''
    return render_template('index.html')

@app.route('/actores')
def actores():
    '''Muestra la lista de actores'''
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/peliculas')
def peliculas():
    '''Muestra la lista de peliculas'''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    '''NMuestra la informacin del un actor'''
    actor = sistema.peliculas[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    return render_template('actor.html', actor=actor, lista_peliculas=personajes)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    '''NMuestra la informacin del un actor'''
    pelicula = sistema.peliculas[id_pelicula]
    actores = sistema.obtener_actores_por_pelicula(id_pelicula)
    return render_template('pelicula.html', pelicula=pelicula, lista_peliculas=actores)

@app.route('/login', methods=['GET', 'POST'])
def login():

    session = {}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exito = sistema.login(username, password)
        if exito:
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre_completo
            return redirect(url_for('index'))
        else:
            error = 'Usuario o Contraseña incorrectos'
            return render_template('login.html')
    return render_template('login.html')

@app.route('/agregar_relacion', methods = ['GET', 'POST'])
def agregar_relacion():
    '''Agrega una relacion entre un actor y una pelicula'''    
    if sistema.usuario_actual is None:
        flash('Debes iniciar sesion para agregar erlaciones', 'warning')
        return redirect(url_for('login'))
    if request.method == 'GET':
        actores_list = []
        for actor in sistema.actores.values():
            actores_list.append({
                'id_estrella': actor.id_estrella,
                'nombre': actor.nombre
            })
            sorted_actores = sorted(actores_list, key=lambda x: x['nombre'])
        peliculas_list = []
        for pelicula in sistema.peliculas.values():
            peliculas_list.append({
            'id_pelicula' : pelicula.id_pelicula,
            'titulo': pelicula.titulo_pelicula
             })    
            sorted_peliculas = sorted(peliculas_list, key = lambda x: x['titulo'])
        return render_template('agregar_relacion.html', actores=sorted_actores, peliculas = sorted_peliculas) 
    if request.method == 'POST':
        id_actor = int(request.form['actorSelect'])
        id_pelicula = int(request.form['movieSelect'])
        personaje = request.form['character']
        sistema.agregar_relacion(id_pelicula, id_actor, personaje)
        sistema.guardar_csv(relaciones_csv, sistema.relaciones)
        flash('relacion agregada correctamente', 'sucess')
        #return redirect(url_for('index'))
        return redirect(url_for('actor', id_actor = id_actor))
  

if __name__ ==  '__main__':
    app.run(debug=True)