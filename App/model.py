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
def new_catalog():
      catalog = {
        'movies': lt.newList('SINGLE_LINKED'),
        'casting': lt.newList('SINGLE_LINKED'),
        'movie_id': mp.newMap(200, maptype='PROBING', loadfactor=0.4, comparefunction=compare_ids)
    }
    return catalog

# Funciones para agregar informacion al catalogo
def add_movies(catalog, movie):
    lt.addLast(catalog['movies'], movie)
    mp.put(catalog['movie_id'], movie['id'], movie)

def add_casting(catalog, movie):
    lt.addLast(catalog['casting'], movie)
    mp.put(catalog['movie_id'], movie['id'], movie)

# ==============================
# Funciones de consulta
# ==============================

def movies_size(catalog):
    return lt.size(catalog['movies'])


def casting_size(catalog):
    return lt.size(catalog['casting'])


# ==============================
# Funciones de Comparacion
# ==============================

def comp_id(id,movies)
    first = lt.getElement(catalog['movies'['id']])
    if id == first:
        return 0
    elif id > first:
        return 1
    else:
        -1