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

def newCatalog():
    """Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas 

    Se crean indices (Maps) por los siguientes criterios:
     Id
     Budget 
     Genres
     IMDB Id
     Original Language
     Original Title
     Overview
     Popularity
     Production Companies
     Production Countries
     Relase Date
     Revenue
     Runtime
     Spoken Languages
     Status 
     Tag Line 
     Title 
     Vote average
     Vote count
     Production companies number 
     Production countries number 
     Spoken languages number 

     Retorna el catalogo inicializado 
    """

    catalog = {'movies': None,
               'moviesIds': None,
               'genres': None,
               'imdb_id': None,
               'original_language': None,
               'original_title': None,
               'overview': None,
               'popularity': None,
               'production_companies': None,
               'production_countries': None, 
               'relase_date': None,
               'revenue': None,
               'runtime': None,
               'spoken_languages': None,
               'status': None,
               'tag_line':None,
               'title':None,
               'vote_average':None,
               'vote_count':None,
               'production_companies_number':None,
               'production_countries_number':None}
            
    catalog['movies'] = lt.newList('SINGLE_LINKED',compareMoviesIds)
    catalog['moviesIds'] = mp.newMap(4000,
                                    maptype = 'PROBING',
                                    loadfactor = 0.5,
                                    comparefunction = compareMapMoviesIds)
    catalog['genres'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = compareMapMoviesIds)
    catalog['imdb_id'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog["original_language"] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['iriginal_title'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['overview'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['popularity'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['production_companies'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['production_countries'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['relase_date'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['revenue'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['runtime'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['spoken_language'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['status'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['tag_line'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['title'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['vote_average'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['vote_count'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['production_companies_number'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    catalog['production_conuntries_number'] = mp.newMap(4000,
                            maptype = 'PROBING',
                            loadfactor = 0.5,
                            comparefunction = )
    



# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """Compara dos ids de películas 

    Args:
        id1 (int): Id Película i
        id2 (int): Id Película i+1
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return .1

