"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
from DISClib.ADT import map as mp
import csv
import model as mdl
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________




# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadMovies():
    lst = mdl.loadCSVFile2("Data/SmallMoviesDetailsCleaned.csv") 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def loadMovies2():
    lst = mdl.loadCSVFile2("Data/MoviesCastingRaw-small.csv") 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def initpeliculas():
    catalogo=mdl.nuevos_mapas()
    return catalogo

def cargar_compañias(catalogo,archivo):
    for elemento in range(1,lt.size(archivo)):
        actual=lt.getElement(archivo,elemento)
        mdl.cargar_compañias(catalogo,actual["production_companies"],actual["title"],actual["vote_average"])
    mapa=catalogo["production_companies"]
    return mapa

def cargar_directores(catalogo,movies,casting):
    for i in range(1,lt.size(movies)):
        actual=lt.getElement(movies,i)
        actual2=lt.getElement(casting,i)
        mdl.cargar_directores(catalogo,actual2["director_name"],actual["title"],actual["vote_average"])
    mapa=catalogo["directores"]
    return mapa

def buscar_director(mapa,nombre):
    retorno=mdl.conocer_director(mapa,nombre)
    return retorno

def cargar_generos(catalogo,archivo,archivo2):
    for i in range(1,lt.size(archivo)):
        actual=lt.getElement(archivo,i)
        mdl.cargar_generos(catalogo,actual["genres"],actual["title"],actual["vote_average"],actual["vote_count"])
    mapa=catalogo["genres"]
    return mapa

def buscar_genero(mapa,genero,mapa2):
    lista=mdl.conocer_genero(mapa,genero,mapa2)
    return lista


def buscar_compañia(mapa,compañia):
    lista=mdl.conocer_compañia(mapa,compañia)
    return lista

def buscar_actores(mapa,actor):
    lista=mdl.conocer_actor(mapa,actor)
    return lista

def buscar_pais(mapa,pais):
    lista=mdl.conocer_pais(mapa,pais)
    return lista

def cargar_actores(catalogo,movies,casting):
    for i in range(1,lt.size(movies)):
        actual=lt.getElement(movies,i)
        actual2=lt.getElement(casting,i)
        mdl.cargar_actores(catalogo,actual2["actor1_name"],actual["title"],actual["vote_average"],actual2["director_name"])
        mdl.cargar_actores(catalogo,actual2["actor2_name"],actual["title"],actual["vote_average"],actual2["director_name"])
        mdl.cargar_actores(catalogo,actual2["actor3_name"],actual["title"],actual["vote_average"],actual2["director_name"])
        mdl.cargar_actores(catalogo,actual2["actor4_name"],actual["title"],actual["vote_average"],actual2["director_name"])
        mdl.cargar_actores(catalogo,actual2["actor5_name"],actual["title"],actual["vote_average"],actual2["director_name"])
    mapa=catalogo["actores"]
    return mapa



def cargar_pais(catalogo,movies,casting):
    for i in range(1,lt.size(movies)):
        actual=lt.getElement(movies,i)
        actual2=lt.getElement(casting,i)
        mdl.cargar_pais(catalogo,actual["production_countries"],actual["title"],actual["release_date"],actual2["director_name"])
    mapa=catalogo["paises"]
    return mapa
       
