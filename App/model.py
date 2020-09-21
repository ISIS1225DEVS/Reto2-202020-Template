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
# ==============================
# Funciones de Comparacion
# ==============================
def getKeyFunction(el1,el2):
    if el1 > el2['key']:
        return 1
    elif el1 < el2['key']:
        return -1
    return 0

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def crearCatalogo(tipo='ARRAY_LIST',cmpfunction=None):
    return lt.newList(tipo,cmpfunction)

def newMap(numelements=17,prime=109345121,maptype='CHAINING',loadfactor=0.5,comparefunction=getKeyFunction):
    return mp.newMap(numelements,prime,maptype,loadfactor,comparefunction)

def crearParejaCatalogo(key,value):
    return me.newMapEntry(key,value)

# Funciones para agregar informacion al catalogo
def agregarFinal(lst,element):
    lt.addLast(lst,element)

def agregarAlMap(mapa,key,value):
    mp.put(mapa,key,value)


# ==============================
# Funciones de consulta
# ==============================
def buscarPeliculas(lst,pos):
    return lt.getElement(lst,pos)

def tamanio(lst):
    return lt.size(lst)

def buscarKeyMap(mapa,key):
    return mp.get(mapa,key)

def setKey(entry,key):
    return me.setKey(entry,key)

def setValue(entry,value):
    return me.setValue(entry,value)

def getKey(entry):
    return me.getKey(entry)

def getValue(entry):
    return me.getValue(entry)