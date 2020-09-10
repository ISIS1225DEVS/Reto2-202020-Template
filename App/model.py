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


#este codiggo se va a utilizar posteriormente para implementar el hashmap
"""
def newCatalog():
    catalog = {'movies': None,
                'id': None,
                'director_name': None,
                'original_language': None,
                'release_date': None}
    catalog['books'] = lt.newList('SINGLE_LINKED', compareBookIds)
    catalog['id'] = mp.newMap(200,
                                    maptype='PROBING',
                                    loadfactor=0.4,
                                    comparefunction=compareMapId)
    catalog['director_name'] = mp.newMap(200,
                                    maptype='PROBING',
                                    loadfactor=0.4,
                                    comparefunction=compareDirectors)
    catalog['original_language'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareLanguage)
    catalog['release_date'] = mp.newMap(500,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareReleaseDate)
    return catalog
"""

# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================
def moviesSize(inputMovies):
    return lt.size(inputMovies)



# ==============================
# Funciones de Comparacion
# ==============================

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file,cmpfunction):
    sep=";"
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
    

    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    
    return lst


def createList():
    lt.newList()

def addMovie(lstmovie, movie):
    lt.addLast(lstmovie, movie)