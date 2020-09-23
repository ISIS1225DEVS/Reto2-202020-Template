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
from DISClib.DataStructures import arraylistiterator as it
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
def catalogo():
    catalogo = {"archivo_peliculas": None,
                "peliculas_por_compañia": None,
                "Peliculas_por_director": None,
                "Peliculas_por_genero":None,
                "peliculas_por_actor":None}


    catalogo["peliculas_por_compañia"] = mp.newMap( numelements=1000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
    catalogo["peliculas_por_director"] = mp.newMap( numelements=1000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
                                                 
    catalogo["archivo_peliculas"] = mp.newMap(numelements=1000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
    catalogo["peliculas_por_genero"] = mp.newMap(numelements=41,
                                                    prime=90537484771,   
                                                    maptype='PROBING', 
                                                    loadfactor=0.5, 
                                                    comparefunction=comparer)
    catalogo["peliculas_por_actor"] = mp.newMap(numelements=2000,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=1.0, 
                                                    comparefunction=comparer)
    return catalogo
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------



# Funciones para agregar informacion al catalogo
def añadir_compañia(catalogo, movie, compañia):
    """
    Añade el nombre de una compañia a la tabla de Hash para compañias en el catalogo
    """
    if mp.contains(catalogo["peliculas_por_compañia"], compañia) == True:
        n = mp.get(catalogo["peliculas_por_compañia"], compañia)
        lt.addLast(me.getValue(n), {"titulo":movie["original_title"], "calificacion":float(movie["vote_average"])})
    else:
        N = lt.newList("ARRAY_LIST")
        lt.addLast(N, {"titulo":movie["original_title"], "calificacion":float(movie["vote_average"])})
        mp.put(catalogo["peliculas_por_compañia"], compañia, N)



def añadir_director(catalogo, movie, director):
    C = catalogo["peliculas_por_director"]
    L = movie["id"]
    if mp.contains(C, director) == False:
        mp.put(catalogo["peliculas_por_director"], director, [])
    añadir_peliculas_al_director(catalogo, L, director)


def añadir_genero(catalogo, movie, generos):
    for a in generos:
        if mp.contains(catalogo["peliculas_por_genero"], a):
            añadir_peliculas_al_genero(catalogo, movie["id"] ,a)
        else:
            D = lt.newList("ARRAY_LIST")
            lt.addLast(D, {"titulo":movie["original_title"], "calificacion":float(movie["vote_average"])})
            mp.put(catalogo["peliculas_por_genero"], a, D)
            

def añadir_actor(catalogo, movie):
    C = {}
    Ana = catalogo["peliculas_por_actor"]
    for a in range(1, 6):
        fila = "actor"+str(a)+"_name"
        actor = movie[fila]
        if mp.contains(Ana, movie[fila]):
            añadir_peliculas_al_actor(catalogo, movie["id"], actor, movie)
        else:
            mp.put(catalogo["peliculas_por_actor"], actor, [])
    






def calificacion(lista):
    N = 0
    B = 0
    A = it.newIterator(lista)
    while it.hasNext(A):
        C = it.next(A)
        N += float(C["calificacion"])
        B += 1
    N = round(N/B, 1)
    return {"Total de peilculas":B,
            "Calificacion promedio":N}



def calificacion2(lista):
    N = 0
    B = 0
    for A in lista:
        K = float(A["calificacion"])
        N += K
        B += 1
    N = round(N/B, 1)
    return {"Total de peilculas":B,
            "Calificacion promedio":N}


def calificacionActor(lista):
    Dire = {}
    N = 0
    B = 0
    mayor = 0
    nombre = None
    for A in lista:
        K = float(A["calificacion"])
        N += K
        B += 1
        if A["Nombre director"] not in Dire:
            Dire[A["Nombre director"]] = 1
        else:
            Dire[A["Nombre director"]] += 1
    for M in Dire:
        if (Dire[M] > mayor):
            mayor = Dire[M]
            nombre = M
        

    N = round(N/B, 1)
    return {"Total de peilculas":B,
            "Calificacion promedio":N,
            "Director con mayor colaboracion":nombre}


def añadir_peliculas_al_director(catalogo, idp, director):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    n = mp.get(catalogo["peliculas_por_director"], director)
    M = me.getValue(n)
    M.append(A)

def añadir_peliculas_al_genero(catalogo, idp, genero):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    n = mp.get(catalogo["peliculas_por_genero"], genero)
    M = me.getValue(n)
    lt.addLast(M, A)

def añadir_peliculas_al_actor(catalogo, idp, actor, movie):
    cat = catalogo["archivo_peliculas"]
    B = mp.get(cat, idp)
    A = me.getValue(B)
    A["Nombre director"] = movie["director_name"]
    n = mp.get(catalogo["peliculas_por_actor"], actor)
    M = me.getValue(n)
    M.append(A)



def addmovie(catalogo, movie):
    A = {"titulo":movie["original_title"],
         "calificacion":movie["vote_average"]}
    mp.put(catalogo["archivo_peliculas"], (movie["id"]), A)


# ==============================
# Funciones de consulta
# ==============================
def mostrar_director(catalogo, Monika):
    if mp.contains(catalogo["peliculas_por_director"], Monika):
        A = mp.get(catalogo["peliculas_por_director"], Monika)
        A = me.getValue(A)
    else:
        A = "No existe ese autor en la base de datos"
    return A

def mostrar_compañias(catalog, Sara):
    if mp.contains(catalog["peliculas_por_compañia"], Sara):
        A = mp.get(catalog["peliculas_por_compañia"], Sara)
        A = me.getValue(A)
    else:
        A ="No existe esa compañia en la base de datos"
    return A

def mostrar_generos(catalogo, Vanesa):
    if mp.contains(catalogo["peliculas_por_genero"], Vanesa):
        A = mp.get(catalogo["peliculas_por_genero"], Vanesa)
        A = me.getValue(A)
    else:
        A ="No existe ese genero en la base de datos"
    return A

def mostrar_actores(catalogo, Juliana):
    if mp.contains(catalogo["peliculas_por_actor"], Juliana):
        A = mp.get(catalogo["peliculas_por_actor"], Juliana)
        A = me.getValue(A)
    else:
        A ="No existe ese actor en la base de datos"
    return A
# ==============================
# Funciones de Comparacion
# ==============================
        
def comparer(keyname, value):
    entry = me.getKey(value)
    if (keyname == entry):
        return 0
    elif (keyname > entry):
        return 1
    else:
        return -1