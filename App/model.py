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
    catalog["Countries"] = mp.newMap(100000,
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
    return director

def newActor(name):

    actor = {"name":"", "movies": None, "average_vote": 0}
    actor["name"] = name
    actor["movies"] = lt.newList("SINGLE_LINKED", compareActors)

def addMovie(catalog, movie):

    lt.addLast(catalog["Movies"], movie)
    mp.put(catalog["MovieIds"], movie["id"], movie)
    addMovieDate(catalog, movie)

def addMovieDate(catalog, movie):

    dates = catalog["Dates"]
    release_date = movie["release_date"]
    existdate = mp.contains(dates, release_date)
    if existdate:
        entry = mp.get(dates, release_date)
        date = me.getValue(entry)
    else:
        date = newDate(release_date)
        mp.put(dates, release_date, date)
    lt.addLast(date["Movies"], movie)

def addCastings(catalog, casting):

    director = casting["director_name"]
    actor1 = casting["actor1_name"]
    actor2 = casting["actor2_name"]
    actor3 = casting["actor3_name"]
    actor4 = casting["actor4_name"]
    actor5 = casting["actor5_name"]
    movieId = casting["id"]
    entry = mp.get(catalog["Movies"], movieId)

    if entry:
        movieCastings = mp.get(catalog["movies"], me.getValue(entry)["name"])

def addDirector(catalog, directorname, movie):

    directors = catalog["directors"]
    existdirector = mp.contains(directors, directorname)
    if existdirector:
        entry = mp.get(directors, directorname)
        director = me.getValue(entry)
    else:
        director = newDirector(directorname)
        mp.put(directors, directorname, director)
    lt.addLast(director["movies"], movie)

    dirAverage = director["average"]
    movieAverage = movie["average_rating"]

    if (dirAverage == 0.0):
        director["average_rating"] = float(movieAverage)
    else:
        director["average_rating"] = (dirAverage + float(movieAverage))/ 2

 
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

def getMoviesByCountry(catalog, country):

    country = mp.get(catalog["Countries"], country)
    if country:
        return me.getValue(country)

def moviesSize(catalog):

    return lt.size(catalog["Movies"])

def directorsSize(catalog):

    return lt.size(catalog["Directors"])

def actorsSize(catalog):
    
    return lt.size(catalog["Actors"])

def getMoviesByGenre(catalog, genre):
    genre = mp.get(catalog["Genres"], genre)    
    if genre:
        return me.getValue(genre)

def genreSize(catalog):
    
    return mp.size(catalog['Genres'])
def getActorsByMovie(catalog, actor_name):
    actor = mp.get(catalog["Actors"], actor_name)
    if actor:
        return me.getValue(actor)
    return None


def newGenre(name):
    genre= {"name": name, "movies":lt.newList("ARRAY_LIST", compare_producers),  ' average_rating':0} 
    return genre

def inputGenre(catalog, genre):
    if genre == None:
        return inputGenre(catalog)
    genre= genre.replace (' ', '') 
    genre= genre.split(',')
    genre= model.inputGenre(catalog,genres)
    return genre
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

def compareCompanies(keyname, entry):

    prodEntry = me.getKey(entry)
    if (keyname == prodEntry):
        return 0
    elif (keyname > prodEntry):
        return 1
    else:
        return -1

def compareAvgVotes(vote1, vote2):

    if float(vote1) == float(vote2):
        return 0
    elif float(vote1) > float(vote2):
        return 1
    else:
        return -1

def compareDirectors(keyname, entry):

    directEntry = me.getKey(director)
    if (keyname == directEntry):
        return 0
    elif (keyname > directEntry):
        return 1
    else:
        return -1

def compareActors(keyname, entry):

    actorEntry = me.getKey(entry)
    if (keyname == actorEntry):
        return 0
    elif (keyname > actorEntry):
        return 1
    else:
        return -1

def compareGenres(keyname, entry):

    genreEntry = me.getKey(entry)
    if (keyname == genreEntry):
        return 0
    elif (keyname > genreEntry):
        return 1
    else:
        return -1

def compareVoteCounts(voteCo1, voteCo2):

    if float(voteCo1) == float(voteCo2):
        return 0
    elif float(voteCo1) > float(voteCo2):
        return 1
    else:
        return -1

def compareCountries(keyname, entry):

    countEntry = me.getKey(entry)
    if keyname == countEntry:
        return 0
    elif keyname > countEntry:
        return 1
    else:
        return -1

def compareDates(date1, date2):

    if (date1) == (date2):
        return 0
    elif (date1) > (date2):
        return 1
    else:
        return -1





