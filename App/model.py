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
from DISClib.DataStructures import listiterator as it
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def comparePeliculas (nombre_pelicula, pelicula):
    if (nombre_pelicula == pelicula['original_title'] ):
        return 0
    else:
        return 1
            
def compareDirectores (Nombre_director, director):
    if (Nombre_director == director['Nombre'] ):
        return 0
    else:
        return 1
def compareGeners(nombre_genero, genero):
    if nombre_genero == genero["Nombre_genero"]:
        return 0
    else:
        return 1

def newCatalog():
   
    catalog = {'Peliculas': None,
               'Directores': None,
               'Generos': None}

    catalog['Peliculas'] = lt.newList('ARRAY_LIST', cmpfunction=comparePeliculas)
    catalog['Directores'] = lt.newList("ARRAY_LIST", cmpfunction=compareDirectores)
    catalog['Generos'] = lt.newList("ARRAY_LIST", cmpfunction=compareGeners)


    return catalog

def nuevo_director(nombre):
    
    director = {'Nombre': "", "Peliculas": None,  "Vote_average": 0}
    director['Nombre'] = nombre
    director['Peliculas'] = lt.newList('ARRAY_LIST')
    return director

def nuevo_genero(nombre_genero):
    
    genero = {'Nombre_genero': "", "Peliculas_genero": None, "Vote_average": 0}
    genero["Nombre_genero"]= nombre_genero
    genero["Peliculas_genero"]=lt.newList("ARRAY_LIST")
    return genero 

def addPeliculaActor(catalog, director_lista, pelicula ):
    
    nombre_director=director_lista["director_name"]
    id1=director_lista["id"]
    id2=pelicula["id"]
    if id1==id2:
        Directores = catalog['Directores']
        existe_director = lt.isPresent(Directores,nombre_director)
        if existe_director > 0:
            director = lt.getElement(Directores,existe_director)
        else:
            director = nuevo_director(nombre_director)
            lt.addLast(Directores,director)   

        lt.addLast(director['Peliculas'], pelicula)

        directorav = director['Vote_average']
        pelicualav = pelicula['vote_average']
        if (directorav == 0.0):
            director['Vote_average'] = float(pelicualav)
        else:
            director['Vote_average'] = (directorav + float(pelicualav)) / 2

def addGenero(catalog,lista_genero,pelicula):
        generos=lista_genero["genres"]
        generos_lista=generos.split("|")
        for genero in generos_lista:
            generoscat=catalog["Generos"]
            existe_genero= lt.isPresent(generoscat,genero)
            if existe_genero > 0:
                generoes=lt.getElement(generoscat,existe_genero)
            else:
                generoes= nuevo_genero(genero)
                lt.addLast(generoscat,generoes)
            lt.addLast(generoes["Peliculas_genero"],pelicula)
            generoav= generoes["Vote_average"]
            pelicualav = pelicula['vote_average']
            if (generoav == 0):
                generoes["Vote_average"]= float(pelicualav)
            else:
                generoes["Vote_average"]= (generoav+float(pelicualav)) / 2
                


def darAutor(catalog,nombre_director):
    existe_director = lt.isPresent(catalog["Directores"],nombre_director)
    autor=lt.getElement(catalog["Directores"],existe_director)
    print(autor)

def darGenero(catalog,nombre_genero):
    existe_genero= lt.isPresent(catalog["Generos"],nombre_genero)
    genero=lt.getElement(catalog["Generos"],existe_genero)
    print("Se encontraron",lt.size(genero["Peliculas_genero"]),"del genero",nombre_genero)

# Funciones para agregar informacion al catalogo

# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


