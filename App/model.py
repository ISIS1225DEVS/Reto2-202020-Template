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
import config
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    catalog = {'details': None,'generos':None, 'compañias': None,}

    catalog['details'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    catalog['generos']  = mp.newMap(36000,loadfactor=1.5,comparefunction=compareGenreByName)
    catalog['compañias'] = mp.newMap(36000,loadfactor=0.4,comparefunction=compareMapName)

    return catalog


def newCompany(name):
    company = {'name': "", "movies": None,  "average_rating": 0}
    company['name'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareMovieIds)
    return company

# Funciones para agregar informacion al catalogo

"""def addGenreMovie(catalog,genres,movie):

    genres = catalog['genres']
    existauthor = mp.contains(genres, genres)
    if existauthor:
        entry = mp.get(genres, genres)
        author = me.getValue(entry)
    else:
        author = newCompany(genres)
        mp.put(genres, genres, author)
    lt.addLast(author['movies'], movie)
"""

def addDetails(catalog, movie):
   
    lt.addLast(catalog['details'], movie)


def addProductoraMovie(catalog, authorname, movie):
    authors = catalog['compañias']
    existauthor = mp.contains(authors, authorname)
    if existauthor:
        entry = mp.get(authors, authorname)
        author = me.getValue(entry)
    else:
        author = newCompany(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(author['movies'], movie)

# ==============================
# Funciones de consulta
# ==============================


def companySize(catalog):
    return mp.size(catalog['compañias'])

def moviesByProductionCompany(catalog, producername):
    producer = mp.get(catalog['compañias'], producername)
    if producer:
        return me.getValue(producer)
    return None

#def moviesByGenre(catalog,genre):
    #genres = mp.get(catalog['genre'], genre)
    #if genres:
        #return me.getValue(genres)
    #return None

def detailSize(catalog):
    resultado = lt.size(catalog['details'])
    return resultado

def encontrarElemento(catalog, posicion):
    primero = lt.getElement(catalog['details'],posicion)
    respuesta = "El título de la película: " + primero["original_title"] + ", " + "La fecha de estreno: " + primero["release_date"] + ", " + "El promedio de la votación: " + primero["vote_average"]+ ", " +"Número de votos: " + primero["vote_count"]+ ", " + "Idioma de la película: " + primero["original_language"]
    return respuesta


# ==============================
# Funciones de Comparacion
# ==============================


def compareMovieIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMapName(keyname, name):
    nameentry = me.getKey(name)
    if (keyname == nameentry):
        return 0
    elif (keyname > nameentry):
        return 1
    else:
        return -1

def compareGenreByName(keyname,genres):

    genentry = me.getKey(genres)
    if (keyname == genentry):
        return 0
    elif (keyname > genentry):
        return 1
    else:
        return -1