import requests
from bs4 import BeautifulSoup
import json

carreras = {
            'IGFO': 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=IGFO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',
            'INBI': 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INBI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',
            'INCE': 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCE&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',
            'INCO': 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INCO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',
            'INNI': 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INNI&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000',
            'INRO': 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=201910&cup=D&majrp=INRO&crsep=&materiap=&horaip=&horafp=&edifp=&aulap=&ordenp=0&mostrarp=1000'
            }

for key, value in carreras.items():
    url = value
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    list = []

    for tr in soup.find_all('tr')[2:-2]:
        data = tr.text.splitlines()
        if len(data) >= 18:
            #Materias con más de un horario
            h = len(data) - 18

            dictionary = {'nrc': data[1],
                          'clave_materia': data[2],
                          'nombre_materia': data[3],
                          'seccion': data[4],
                          'creditos': data[5],
                          'cupos': data[6],
                          'cupos_disponibles': data[7],
                          'ciclo': '2019/01/16-2019/05/31',
                          'profesor': data[h+16]
                          }

            horarios = []
            dias =[]
            edificios =[]
            aulas = []

            ciclo = False
            for i in range(h+1):
                e = 0
                horarios.append(data[i+11][2:6] + "-" + data[i+11][7:11])
                dias.append(data[i+11][11:22])

                # Alpha y Beta
                if data[i+11][22:26] == 'DUCT':
                    e = 1

                edificios.append(data[i+11][22:e + 26])
                aulas.append(data[i+11][e + 26:e + 30])

            dictionary.update({'horario': horarios})
            dictionary.update({'dias': dias})
            dictionary.update({'edificio': edificios})
            dictionary.update({'aula': aulas})
            list.append(dictionary)

    with open(key + '.json', 'w') as file:
        json.dump(list, file, sort_keys=False, indent=4)
