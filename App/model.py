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
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as iter

import csv

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
def getKeyFunction(el1,el2):
    if el1 > el2['key']:
        return 1
    elif el1 < el2['key']:
        return -1
    return 0
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog (file1, file2):
    lst = lt.newList("ARRAY_LIST")
    dialect = csv.excel()
    dialect.delimiter=";"
    
    with open(cf.data_dir + file1, encoding="utf-8-sig") as csvfile1:
        row = csv.DictReader(csvfile1, dialect=dialect)
        for elemento in row:
            lt.addLast(lst,elemento)
    with open(cf.data_dir + file2, encoding="utf-8-sig") as csvfile2: #Cambiamos el encoding ya que generaba
        row = csv.DictReader(csvfile2,dialect=dialect)                
        i = 1
        for elemento in row:
            if elemento["id"] == lt.getElement(lst,i)["id"]:
                for column in elemento:
                    if column != "id":
                        lt.getElement(lst,i)[column] = elemento[column]
            i += 1


    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")  
    return lst

# Funciones para agregar informacion al catalogo


def addMovie(map,llave,movie):
    mp.put(map,llave,movie)

def moviesByProductionCompany (lst, companyname):
    productionCompanyMAP = model.crearMap()
    iterator = iter.newIterator(lst)
    while iter.hasNext(iterator):
        if iter.next(iterator)['production_companies'] == companyname:#list[i]['production company'] == companyname:
            addMovie(moviesByProductionCompany, map[key])
    return moviesByProductionCompany
def crearMap():
    return mp.newMap(comparefunction=getKeyFunction)

def obtenerLlave(map, llave):
    return mp.get(map,llave)
    


def moviesByCountry (countryname):
    pass

def moviesByDirector (directorname):
    pass

def moviesByActor (actorname):
    pass

def moviesByGenre (genre):
    pass


# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1

