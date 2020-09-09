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



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


#===============================
def newList():
    a = lt.newList()
    return a

def addLast(lst, element):
    lt.addLast(lst, element)

def giveSize(lst):
    size = lt.size(lst)
    return size

def getFirstElement(lst):
    first_element=lt.firstElement(lst)
    return first_element

def getLastElement(lst):
    last_element=lt.lastElement(lst)
    return last_element

def getTitle(element):
    return element["original_title"]
    
def getDate(element):
    return element["release_date"]

def getAverage(element):
    return element["vote_average"]

def getVotes(element):
    return element["vote_count"]

def getLang(element):
    return element["original_language"]