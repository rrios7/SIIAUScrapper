from flask import Flask, jsonify
app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '', database = 'oferta_academica')
cursor = conexion.cursor()

query = 'SELECT * FROM materia'
cursor.execute(query)
materias = cursor.fetchall()

query = 'SELECT * FROM profesor'
cursor.execute(query)
profesores = cursor.fetchall()

query = 'SELECT * FROM aula'
cursor.execute(query)
aulas = cursor.fetchall()

query = 'SELECT * from edificio'
cursor.execute(query)
edificios = cursor.fetchall()

query = 'SELECT * FROM seccion'
cursor.execute(query)
secciones = cursor.fetchall()

query = 'SELECT * FROM ciclo'
cursor.execute(query)
ciclos = cursor.fetchall()

query = 'SELECT * FROM horario'
cursor.execute(query)
horarios = cursor.fetchall()

query = 'SELECT * FROM dias'
cursor.execute(query)
dias = cursor.fetchall()

def agregarCursos(cursos):
    lista_cursos = []
    dict_cursos = {'oferta': lista_cursos}

    for curso in cursos:
        c = {
            'nrc': curso[1],
            'cupos': curso[2],
            'cupos_disponibles': curso[3],
            'clave_materia': materias[curso[4] - 1][1],
            'nombre_materia': materias[curso[4] - 1][2],
            'creditos': materias[curso[4] - 1][3],
            'seccion': secciones[curso[5] - 1][1],
            'profesor': profesores[curso[6] - 1][1],
            'ciclo': ciclos[curso[7] - 1][1]
        }

        query = 'SELECT * FROM agenda_curso WHERE id_curso = %s'
        cursor.execute(query, (curso[0],))
        agendas = cursor.fetchall()

        lista_horarios = []
        lista_dias = []
        lista_edificios = []
        lista_aulas = []

        for agenda in agendas:
            lista_horarios.append(horarios[agenda[1]-1][1])
            lista_dias.append(dias[agenda[2]-1][1])
            lista_edificios.append(edificios[aulas[agenda[3]-1][2] - 1][1])
            lista_aulas.append(aulas[agenda[3]-1][1])

        c.update({'horario': lista_horarios})
        c.update({'dias': lista_dias})
        c.update({'edificio': lista_edificios})
        c.update({'aula': lista_aulas})

        lista_cursos.append(c)
    return jsonify(dict_cursos)

@app.route('/api/glob')
def show_glob():
    query = 'SELECT * FROM curso;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

@app.route('/api/igfo')
def show_igfo():
    query = 'SELECT * FROM curso, catalogo_carrera WHERE id = id_curso AND id_carrera = 1;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

@app.route('/api/inbi')
def show_inbi():
    query = 'SELECT * FROM curso, catalogo_carrera WHERE id = id_curso AND id_carrera = 2;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

@app.route('/api/ince')
def show_ince():
    query = 'SELECT * FROM curso, catalogo_carrera WHERE id = id_curso AND id_carrera = 3;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

@app.route('/api/inco')
def show_inco():
    query = 'SELECT * FROM curso, catalogo_carrera WHERE id = id_curso AND id_carrera = 4;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

@app.route('/api/inni')
def show_info():
    query = 'SELECT * FROM curso, catalogo_carrera WHERE id = id_curso AND id_carrera = 5;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

@app.route('/api/inro')
def show_inro():
    query = 'SELECT * FROM curso, catalogo_carrera WHERE id = id_curso AND id_carrera = 6;'
    cursor.execute(query)
    cursos = cursor.fetchall()

    return agregarCursos(cursos)

app.run()