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
# API del TAD Catalogo de películas.
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de películas

    Crea una lista vacia para guardar todas las películas.

    Se crean indices (Maps) por los siguientes criterios:
    ID películas

    Retorna el catálogo inicializado.
    """
    catalog = {
        'details': lt.newList('SINGLE_LINKED'),
        'casting': lt.newList('SINGLE_LINKED'),
        'movies_ids': mp.newMap(200, maptype='PROBING', loadfactor=0.4)
    }
    return catalog


# Funciones para agregar informacion al catalogo
def add_details(catalog, movie):
    """
    Esta funcion adiciona detalles a la lista de películas,
    adicionalmente los guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['details'], movie)
    mp.put(catalog['movies_ids'], movie['id'], movie)


def add_casting(catalog, movie):
    """
    Esta funcion adiciona un elenco a la lista de películas,
    adicionalmente lo guarda en un Map usando como llave su Id.
    """
    lt.addLast(catalog['casting'], movie)
    mp.put(catalog['movies_ids'], movie['id'], movie)


# ==============================
# Funciones de consulta
# ==============================
def details_size(catalog):
    # Número de detalles en el catálogo.
    return lt.size(catalog['details'])


def casting_size(catalog):
    # Número de elencos en el catálogo.
    return lt.size(catalog['casting'])
