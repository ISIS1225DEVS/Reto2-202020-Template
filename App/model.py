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

def compareActoresByName(keyname, actor):
    direntry = me.getKey(actor)
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

def comparegenres_vote(keyname, vote):
    direntry = me.getKey(vote)
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

def comparepais(keyname,pais):
    direntry = me.getKey(pais)
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
    peliculas["production_companies"]=mp.newMap(20030,20111,maptype='CHAINING',loadfactor=0.9,comparefunction=compareproductor)
    peliculas["directores"]=mp.newMap(20030,20111,maptype='CHAINING',loadfactor=0.9,comparefunction=compareDirectorsByName)
    peliculas["genres"]=mp.newMap(20030,20111,maptype='CHAINING',loadfactor=0.9,comparefunction=comparegenres)
    peliculas["actores"]=mp.newMap(20030,20111,maptype='CHAINING',loadfactor=0.9,comparefunction=compareActoresByName)
    peliculas["paises"]=mp.newMap(20030,20111,maptype='CHAINING',loadfactor=0.9,comparefunction=comparepais)
    peliculas["genres_vote"]=mp.newMap(20030,20111,maptype='CHAINING',loadfactor=0.9,comparefunction=comparegenres_vote)
    
    return peliculas

def cargar_compañias(catalogo,compañia,valor,promedio):
    mapa=catalogo["production_companies"]
    pareja=mp.get(mapa,compañia)
    if pareja==None:
        #print("Nuevo director",director,pelicula)
        lista=lt.newList(datastructure="SINGLE_LINKED")
        lt.addFirst(lista,(valor,promedio))
        mp.put(mapa,compañia,lista)

    else:
        #print("Director existe",director,pelicula)
        lt.addLast(pareja["value"],(valor,promedio))

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

def cargar_generos(catalogo,genre,pelicula,promedio,vote):
    mapa=catalogo["genres"]
    mapa2=catalogo["genres_vote"]
    pareja=mp.get(mapa,genre)
    pareja2=mp.get(mapa2,genre)
    if pareja==None:
        #print("Nuevo director",director,pelicula)
        lista=lt.newList(datastructure="SINGLE_LINKED")
        lt.addFirst(lista,(pelicula,promedio))
        mp.put(mapa,genre,lista)

    else:
        
        lt.addLast(pareja["value"],(pelicula,promedio))
    if pareja2==None:
        mp.put(mapa2,genre,float(vote))
    else:
        pareja2["value"]+=float(vote)

        
        




def cargar_actores(catalogo,actor,pelicula,promedio,director):
    if actor != None:
        mapa=catalogo["actores"]
        pareja=mp.get(mapa,actor)
        if pareja==None:
            lista=lt.newList(datastructure="SINGLE_LINKED")
            lt.addFirst(lista,(pelicula,promedio,director))
            mp.put(mapa,actor,lista)
        else:
            lt.addLast(pareja["value"],(pelicula,promedio,director))

def cargar_pais(catalogo,pais,pelicula,promedio,director):
    mapa=catalogo["paises"]
    pareja=mp.get(mapa,pais)
    if pareja==None:
        #print("Nuevo actor",actor,pelicula)
        lista=lt.newList(datastructure="SINGLE_LINKED")
        lt.addFirst(lista,(pelicula,promedio,pais))
        mp.put(mapa,pais,lista)

    else:
        #print("Director existe",director,pelicula)

        lt.addLast(pareja["value"],(pelicula,promedio,pais))


def conocer_director(mapa,director):
    lista=mp.get(mapa,director)
    direc=me.getValue(lista)
    paso=direc["first"]
    promedio=0
    while paso != None:
        promedio+=float(paso["info"][1])
        paso=paso["next"]
    promedio=promedio/direc["size"]
    respuesta={"lista":lista,"promedio_total":round(promedio,2),"total_de_peliculas":direc["size"]}

    return respuesta
    

def conocer_genero(mapa,genero,mapa2):
    
    lista=mp.get(mapa,genero)
    gen=me.getValue(lista)
    paso=gen["first"]
    promedio=0
    while paso != None:
        promedio+=float(paso["info"][1])
        paso=paso["next"]
    promedio=promedio/gen["size"]
    respuesta={"lista":lista,"promedio_total_de_las_peliculas":round(promedio,2),"total_de_peliculas":gen["size"],"promedio_de_votos_del_genero":(me.getValue(mp.get(mapa2,genero))/gen["size"])}
    return respuesta

def conocer_compañia(mapa,compañia):
    lista=mp.get(mapa,compañia)
    com=me.getValue(lista)
    paso=com["first"]
    promedio=0
    while paso != None:
        promedio+=float(paso["info"][1])
        paso=paso["next"]
    promedio=promedio/com["size"]
    respuesta={"lista":lista,"promedio_total_de_las_peliculas":round(promedio,2),"total_de_peliculas":com["size"]}
    return respuesta
    

def conocer_actor(mapa,actor):
    lista=mp.get(mapa,actor)
    ac=me.getValue(lista)
    paso=ac["first"]
    promedio=0
    directores={}
    while paso!= None:
        promedio+=float(paso["info"][1])
        if paso["info"][2] not in directores.keys():
            directores[paso["info"][2]]=1
        else:
            directores[paso["info"][2]]+=1
        paso=paso["next"]
    promedio=promedio/ac["size"]
    mayor=0
    mejor=None
    for director in directores.keys():
        if directores[director] > mayor:
            mayor=directores[director] 
            mejor=director

        
    respuesta={"lista":lista,"promedio_total":round(promedio,2),"total_de_peliculas":ac["size"],"director_con_mas_colaboraciones":mejor}

    return respuesta
    

def conocer_pais(mapa,pais):
    lista=mp.get(mapa,pais)
    return lista



