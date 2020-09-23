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
import csv

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


def compareDirectorsByName(keyname, director):
    direntry = me.getKey(director)
    if (keyname == direntry):
        return 0
    elif (keyname > direntry):
        return 1
    else:
        return -1

def comparegenres(keyname, genre):
    direntry = me.getKey(genre)
    if (keyname == direntry):
        return 0
    elif (keyname > direntry):
        return 1
    else:
        return -1

def compareproductor(keyname, productor_companie):
    direntry = me.getKey(productor_companie)
    if (keyname == direntry):
        return 0
    elif (keyname > direntry):
        return 1
    else:
        return -1



def loadCSVFile2 (file, sep=";"):
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
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


def nuevos_mapas():
    peliculas={"directores":None,"production_companies":None,"genres":None}
    peliculas["production_companies"]=mp.newMap(2003,2011,maptype='CHAINING',loadfactor=0.9,comparefunction=compareproductor)
    peliculas["directores"]=mp.newMap(2003,2011,maptype='CHAINING',loadfactor=0.9,comparefunction=compareDirectorsByName)
    peliculas["genres"]=mp.newMap(2003,2011,maptype='CHAINING',loadfactor=0.9,comparefunction=comparegenres)
    return peliculas

def cargar_compañias(catalogo,compañia,valor):
    mapa=catalogo["production_companies"]
    pareja=mp.get(mapa,compañia)
    if pareja==None:
        #print("Nuevo director",director,pelicula)
        lista=lt.newList(datastructure="SINGLE_LINKED")
        lt.addFirst(lista,valor)
        mp.put(mapa,compañia,lista)

    else:
        #print("Director existe",director,pelicula)
        lt.addLast(pareja["value"],valor)

def cargar_directores(catalogo,director,pelicula,promedio):
    mapa=catalogo["directores"]
    pareja=mp.get(mapa,director)
    if pareja==None:
        #print("Nuevo director",director,pelicula)
        lista=lt.newList(datastructure="SINGLE_LINKED")
        lt.addFirst(lista,(pelicula,promedio))
        mp.put(mapa,director,lista)

    else:
        #print("Director existe",director,pelicula)
        lt.addLast(pareja["value"],(pelicula,promedio))

def cargar_generos(catalogo,genre,pelicula,promedio):
    mapa=catalogo["genres"]
    pareja=mp.get(mapa,genre)
    if pareja==None:
        #print("Nuevo director",director,pelicula)
        lista=lt.newList(datastructure="SINGLE_LINKED")
        lt.addFirst(lista,(pelicula,promedio))
        mp.put(mapa,genre,lista)

    else:
        #print("Director existe",director,pelicula)
        lt.addLast(pareja["value"],(pelicula,promedio))

def conocer_director(mapa,director):
    lista=mp.get(mapa,director)
    return lista

def conocer_genero(mapa,genero):
    lista=mp.get(mapa,genero)
    return lista

def conocer_compañia(mapa,compañia):
    lista=mp.get(mapa,compañia)
    return lista
