import glob
import json
import mysql.connector

conexion = mysql.connector.connect(
    user='root',
    password='',
    database='oferta_academica')
cursor = conexion.cursor()

files = glob.glob('*.json')

#Materia
def existe_materia(c):
    select = 'SELECT * FROM materia WHERE clave = %s'
    cursor.execute(select, (c['clave_materia'],))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_materia(c):
    insert = 'INSERT INTO materia(clave, nombre, creditos) VALUES(%s, %s, %s)'
    cursor.execute(insert, (c['clave_materia'], c['nombre_materia'], c['creditos'],))
    conexion.commit()
    return cursor.lastrowid

def get_id_materia(c):
    select = 'SELECT id from materia WHERE clave = %s'
    cursor.execute(select, (c['clave_materia'],))

    rows = cursor.fetchall()
    return rows[0][0]

#Seccion
def existe_seccion(c):
    select = 'SELECT * FROM seccion WHERE nombre = %s '
    cursor.execute(select, (c['seccion'],))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_seccion(c):
    insert = 'INSERT INTO seccion(nombre) VALUES(%s)'
    cursor.execute(insert, (c['seccion'],))
    conexion.commit()
    return cursor.lastrowid

def get_id_seccion(c):
    select = 'SELECT id from seccion WHERE nombre = %s'
    cursor.execute(select, (c['seccion'],))

    rows = cursor.fetchall()
    return rows[0][0]

#Profesor
def existe_profesor(c):
    select = 'SELECT * FROM profesor WHERE nombre = %s '
    cursor.execute(select, (c['profesor'],))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_profesor(c):
    insert = 'INSERT INTO profesor(nombre) VALUES(%s)'
    cursor.execute(insert, (c['profesor'],))
    conexion.commit()
    return cursor.lastrowid

def get_id_profesor(c):
    select = 'SELECT id from profesor WHERE nombre = %s'
    cursor.execute(select, (c['profesor'],))

    rows = cursor.fetchall()
    return rows[0][0]

#Edificio
def existe_edificio(edificio):
    select = 'SELECT * FROM edificio WHERE nombre = %s '
    cursor.execute(select, (edificio,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_edificio(edificio):
    insert = 'INSERT INTO edificio(nombre) VALUES(%s)'
    cursor.execute(insert, (edificio,))
    conexion.commit()
    return cursor.lastrowid

def get_id_edificio(edificio):
    select = 'SELECT id from edificio WHERE nombre = %s'
    cursor.execute(select, (edificio,))
    rows = cursor.fetchall()

    return int(rows[0][0])

#Aula
def existe_aula(aula, id_edificio):
    select = 'SELECT * FROM aula WHERE nombre = %s'
    cursor.execute(select, (aula,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        for aula in rows:
            if aula[2] == id_edificio:
                return True
        return False
    else:
        return False

def insertar_aula(aula, id_edificio):
    insert = 'INSERT INTO aula(nombre, id_edificio) VALUES(%s, %s)'
    cursor.execute(insert, (aula, id_edificio,))
    conexion.commit()
    return cursor.lastrowid

def get_id_aula(aula, id_edificio):
    select = 'SELECT * from aula WHERE nombre = %s'
    cursor.execute(select, (aula,))

    rows = cursor.fetchall()

    for aula in rows:
        if aula[2] == id_edificio:
            return aula[0]

#Ciclo
def existe_ciclo(c):
    select = 'SELECT * FROM ciclo WHERE datos = %s'
    cursor.execute(select, (c['ciclo'],))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_ciclo(c):
    insert = 'INSERT INTO ciclo(datos) VALUES(%s)'
    cursor.execute(insert, (c['ciclo'],))
    conexion.commit()
    return cursor.lastrowid

def get_id_ciclo(c):
    select = 'SELECT id from ciclo WHERE datos = %s'
    cursor.execute(select, (c['ciclo'],))

    rows = cursor.fetchall()
    return rows[0][0]

#Horario
def existe_horario(datos):
    select = 'SELECT * FROM horario WHERE datos = %s'
    cursor.execute(select, (datos,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_horario(datos):
    insert = 'INSERT INTO horario(datos) VALUES(%s)'
    cursor.execute(insert, (datos,))
    conexion.commit()
    return cursor.lastrowid

def get_id_horario(datos):
    select = 'SELECT id from horario WHERE datos = %s'
    cursor.execute(select, (datos,))

    rows = cursor.fetchall()
    return rows[0][0]

#Dias
def existe_dias(dias):
    select = 'SELECT * FROM dias WHERE datos = %s '
    cursor.execute(select, (dias,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_dias(dias):
    insert = 'INSERT INTO dias(datos) VALUES(%s)'
    cursor.execute(insert, (dias,))
    conexion.commit()
    return cursor.lastrowid

def get_id_dias(dias):
    select = 'SELECT id from dias WHERE datos = %s'
    cursor.execute(select, (dias,))

    rows = cursor.fetchall()
    return rows[0][0]

#Cursos
def existe_curso(c):
    select = 'SELECT * FROM curso WHERE nrc = %s'
    cursor.execute(select, (c['nrc'],))
    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_curso(c, id_materia, id_seccion, id_profesor, id_ciclo):
    insert = 'INSERT INTO curso(nrc, ' \
             'cupos, cupos_disponibles, id_materia, id_seccion, id_profesor, id_ciclo)' \
             'VALUES(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(insert, (c['nrc'],
                            c['cupos'],
                            c['cupos_disponibles'],
                            id_materia,
                            id_seccion,
                            id_profesor,
                            id_ciclo))
    conexion.commit()
    return cursor.lastrowid

def get_id_curso(c):
    select = 'SELECT id from curso WHERE nrc = %s'
    cursor.execute(select, (c['nrc'],))

    rows = cursor.fetchall()
    return rows[0][0]

#Agenda del Curso
def existe_agenda(id_curso, id_horario, id_dias, id_aula):
    select = 'SELECT * from agenda_curso WHERE id_curso = %s AND id_horario = %s AND id_dias = %s AND id_aula = %s'
    cursor.execute(select, (id_curso, id_horario, id_dias, id_aula,))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        False

def insertar_agenda(id_curso, id_horario, id_dias, id_aula):
    insert = 'INSERT INTO agenda_curso(id_curso, id_horario, id_dias, id_aula) VALUES (%s, %s, %s, %s)'
    cursor.execute(insert, (id_curso, id_horario, id_dias, id_aula))

    conexion.commit()

#Carrera
def existe_carrera(f):
    select = 'SELECT * from carrera WHERE nombre = %s'
    cursor.execute(select, (f[:4],))

    rows = cursor.fetchall()

    if len(rows) > 0:
        return True
    else:
        return False

def insertar_carrera(f):
    insert = 'INSERT INTO carrera(nombre) VALUES(%s)'
    cursor.execute(insert, (f[:4],))

    conexion.commit()
    return cursor.lastrowid

def get_id_carrera(f):
    select = 'SELECT id from carrera WHERE nombre = %s'
    cursor.execute(select, (f[:4],))

    rows = cursor.fetchall()
    return rows[0][0]

#Catalogo Carrera
def existe_catalogo_carrera(id_curso, id_carrera):
    select = 'SELECT * from catalogo_carrera WHERE id_curso = %s AND id_carrera = %s'
    cursor.execute(select, (id_curso, id_carrera,))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        False

def insertar_catalogo_carrera(id_curso, id_carrera):
    insert = 'INSERT INTO catalogo_carrera(id_curso, id_carrera) VALUES (%s, %s)'
    cursor.execute(insert, (id_curso, id_carrera,))

    conexion.commit()

for file in files:
    with open(file, encoding='utf-8') as f:
        cursos = json.load(f)
        for curso in cursos:
            id_materia = 0
            id_seccion = 0
            id_profesor = 0
            id_horario = 0
            id_ciclo = 0
            id_edificio = 0
            id_aula = 0
            id_dias = 0
            id_curso = 0
            id_carrera = 0

            if not existe_materia(curso):
                id_materia = insertar_materia(curso)
            else:
                id_materia = get_id_materia(curso)

            if not existe_seccion(curso):
                id_seccion = insertar_seccion(curso)
            else:
                id_seccion = get_id_seccion(curso)

            if not existe_profesor(curso):
                id_profesor = insertar_profesor(curso)
            else:
                id_profesor = get_id_profesor(curso)

            if not existe_ciclo(curso):
                id_ciclo = insertar_ciclo(curso)
            else:
                id_ciclo = get_id_ciclo(curso)

            if not existe_curso(curso):
                id_curso = insertar_curso(curso, id_materia, id_seccion, id_profesor, id_ciclo)
            else:
                id_curso = get_id_curso(curso)

            for i in range(len(curso['edificio'])):
                if not existe_edificio(curso['edificio'][i]):
                    id_edificio = insertar_edificio(curso['edificio'][i])
                else:
                    id_edificio = get_id_edificio(curso['edificio'][i])

                if not existe_aula(curso['aula'][i], id_edificio):
                    id_aula = insertar_aula(curso['aula'][i], id_edificio)
                else:
                    id_aula = get_id_aula(curso['aula'][i], id_edificio)

                if not existe_horario(curso['horario'][i]):
                    id_horario = insertar_horario(curso['horario'][i])
                else:
                    id_horario = get_id_horario(curso['horario'][i])

                if not existe_dias(curso['dias'][i]):
                    id_dias = insertar_dias(curso['dias'][i])
                else:
                    id_dias = get_id_dias(curso['dias'][i])

                if not existe_agenda(id_curso, id_horario, id_dias, id_aula):
                    insertar_agenda(id_curso, id_horario, id_dias, id_aula)

            if not existe_carrera(file):
                id_carrera = insertar_carrera(file)
            else:
                id_carrera = get_id_carrera(file)

            if not existe_catalogo_carrera(id_curso, id_carrera):
                insertar_catalogo_carrera(id_curso, id_carrera)