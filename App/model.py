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
    
    catalog = {"Movies": None,
                "ProdCompanies": None,
                "AvgVote": None,
                "Directors": None,
                "Actors": None,
                "Genres": None,
                "VoteCounts": None,
                "ProdCountries": None,
                "Dates": None}
    
    catalog["Movies"] = lt.newList("SINGLED_LINKED", compareMovieIds)
    catalog["MovieIds"] = mp.newMap(100000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareMapMovieIds)
    catalog["ProdCompanies"] = mp.newMap(100000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareProdCompanies)
    catalog["AvgVote"] = mp.newMap(100000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareAvgVotes)
    catalog["Directors"] = mp.newMap(100000,
                                maptype="PROBING",
                                loadfactor=0.4,
                                comparefunction=compareDirectors)
    catalog["Actors"] = mp.newMap(100000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareActors)
    catalog["Genres"] = mp.newMap(100000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareGenres)
    catalog["VoteCounts"] = mp.newMap(100000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareVoteCounts)
    catalog["ProdCountries"] = mp.newMap(100000,
                                        maptype="PROBING",
                                        loadfactor=0.4,
                                        comparefunction=compareCountries)
    catalog["Dates"] = mp.newMap(100000,
                                maptype="PROBING",
                                loadfactor=0.4,
                                comparefunction=compareDates)
    
    return catalog
# Funciones para agregar informacion al catalogo

def newDirector(name):

    director = {"name":"", "movies": None, "average_vote": 0}
    director["name"] = name
    director["movies"] = lt.newList("SINGLE_LINKED", compareDirectorsByName)

def addMovie(catalog, movie):

    lt.addLast(catalog["Movies"], movie)
    mp.put(catalog["MovieIds"], movie["movie_details_id"], movie)
    addMovieDate(catalog, movie)

def addMovieDate(catalog, movie):

    dates = catalog["Dates"]
    release_date = movie["release_date"]
    existdate = mp.contains(date, release_date)
    if existdate:
        entry = mp.get(dates, release_date)
        date = me.getValue(entry)
    else:
        date = newDate(release_date)
        mp.put(dates, release_date, date)
    lt.addLast(date["Movies"], movie)

def newDate(release_date):
    
    entry = {"Date": "", "Movies": None}
    entry["Date"] = release_date
    entry["Movies"] = lt.newList("SINGLE_LINKED", compareDates)
    return entry


# ==============================
# Funciones de consulta
# ==============================

def getMoviesByDirector(catalog,directorName):

    director = mp.get(catalog["Directors"], directorName)
    if director:
        return me.getValue(director)
    return None

def getMoviesByDate(catalog, date):

    date = mp.get(catalog["Dates"], date)
    if date:
        return me.getValue(date)["Movies"]
    return None

def moviesSize(catalog):

    return lt.size(catalog["Movies"])

def directorsSize(catalog):

    return lt.size(catalog["Directors"])

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

def compareMapMovieIds(id, entry):

    idEntry = me.getKey(entry)
    if (int(id) == int(idEntry)):
        return 0
    elif (int(id) > int(idEntry)):
        return 1
    else:
        return -1

def compareProdCompanies(keyname, entry):

    prodEntry = me.getKey(entry)
    if (keyname == prodEntry):
        return 0
    elif (keyname > prodEntry):
        return 1
    else:
        return -1

def compareDirectors(keyname, director):

    directEntry = me.getKey(director)
    if (keyname == directEntry):
        return 0
    elif (keyname > directEntry):
        return 1
    else:
        return -1

def compareDates(date1, date2):

    if (date1) == (date2):
        return 0
    elif (date1) > (date2):
        return 1
    else:
        return 0





