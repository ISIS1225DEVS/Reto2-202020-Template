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
# API del TAD Catalogo de peliculas
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de peliculas

    Crea una lista vacia para guardar todos los peliculas

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'Movies': None,
               'production_companies': None,
               'director_name': None,
               'actor_name': None,
               'genre': None,
               'production_countries': None}

    catalog['id'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog["MoviesId"] = mp.newMap(2000,
                                    maptype='PROBING', # No entiendo
                                    loadfactor=0.4,  # No entiendo
                                    comparefunction=compareMapMoviesIds) #No entiendo
    catalog['production_companies'] = mp.newMap(2000,
                                                maptype='PROBING',  # Esto no lo entiendo
                                                loadfactor=0.4,    #Esto no lo entiendo
                                                comparefunction=compareCompanies) #Esto lo entiendo mas pero tampoco lo entiendo
    catalog['director_name'] = mp.newMap(2000,
                                         maptype='PROBING', #No lo entiendo
                                         loadfactor=0.4, #No entiendo
                                         comparefunction=compareDirectorsByName) #No entiendo
    catalog['actor_name'] = mp.newMap(2000,
                                      maptype='CHAINING', #No entiendo
                                      loadfactor=0.7, #No entiendo
                                      comparefunction=compareActorsByNames) # No entiendo
    catalog['genre'] = mp.newMap(2000,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareByGenre)
    catalog['production_countries'] = mp.newMap(2000,
                                                maptype='CHAINING',
                                                loadfactor=0.7,
                                                comparefunction=compareCountries)

    return catalog


# Funciones para agregar informacion al catalogo

def addMovie():
    return 0

def addMovieCompanie():
    return 0

def addMovieCountry():
    return 0

def addMovieGenre():
    return 0

def addCasting():
    return 0

def addCastingActor():
    return 0

def addCastingDirector():
    return 0



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
def compareCompanies():
    return 0
def compareDirectorsByName():
    return 0
def compareByGenre():
    return 0
def compareCountries():
    return 0
def compareActorsByNames():
    return 0 