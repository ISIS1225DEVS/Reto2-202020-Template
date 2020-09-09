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



# Funciones para agregar informacion al catalogo
def newCatalog (file1, file2, compareRecordIds):
    lst = lt.newCatalog()
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file1, encoding="utf-8-sig") as csvfile1:
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

    except:
        print("Hubo un error con la carga del archivo")

    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    print(lt.firstElement(lst))
    print(lt.lastElement(lst)))    
    return lst

def addMovie (movie):
    pass

def moviesByProductionCompany (companyname):
    pass

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

