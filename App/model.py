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
# API del TAD Catalogo de Peliculas
# -----------------------------------------------------

def newCatalog():
    catalog = {'movies': None,
               'production companies': None}
    catalog["movies"] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog["production companies"]=mp.newMap(2000,
                                              maptype="CHAINING",
                                              loadfactor=0.5,
                                              comparefunction=compareCompaniesByName)
    return catalog

def newCompany(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    production_comp = {'name': "", "movies": None,  "average_rating": 0}
    production_comp["name"] = name
    production_comp["movies"] = lt.newList('SINGLE_LINKED', compareCompaniesByName)
    return production_comp

# Funciones para agregar informacion al catalogo

def addMovie(catalog, movie):
    lt.addLast(catalog["movies"], movie)

def addProductionCompany(catalog, companyname, movie):
    """
    Esta función adiciona una compañia a la lista de peliculas publicadas
    por una compañia.
    Cuando se adiciona la compañia se actualiza el promedio de dicha compañia
    """
    production_comp = catalog["production companies"]
    compname = movie["production_companies"]
    existcomp = mp.contains(production_comp, compname)
    if existcomp:
        entry = mp.get(production_comp, compname)
        company = me.getValue(entry)
    else:
        company = newCompany(compname)
        mp.put(production_comp, companyname, company)
    lt.addLast(company["movies"], movie)

    compavg = company["average_rating"]
    movieavg = movie["vote_average"]
    if (compavg == 0.0):
        company["average_rating"] = float(movieavg)
    else:
        company["average_rating"] = (compavg + float(movieavg)) / 2

# ==============================
# Funciones de consulta
# ==============================

def moviesByProductionCompany(catalog, compname):
    """
    Retorna una productora de cine con sus peliculas a partir del nombre de la productora
    """
    company = mp.get(catalog["production companies"], compname)
    if company:
        return me.getValue(company)
    return None

def moviesSize(catalog):
    """
    Número de peliculas en el catalogo
    """
    return lt.size(catalog)

def companiesSize(catalog):
    """
    Numero de autores en el catalogo
    """
    return mp.size(catalog["production companies"])

# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de peliculas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareCompaniesByName(keyname, company):
    """
    Compara dos nombres de compañia de produccion. El primero es una cadena
    y el segundo un entry de un map
    """
    compentry = me.getKey(company)
    if (keyname == compentry):
        return 0
    elif (keyname > compentry):
        return 1
    else:
        return -1
