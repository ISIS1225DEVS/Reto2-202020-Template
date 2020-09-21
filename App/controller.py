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
from App import model
import csv
from DISClib.DataStructures import listiterator as iter

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
getKeyFunction = model.getKeyFunction
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def iniciarCatalogo():
    return model.crearCatalogo()

def crearHash(tipo='CHAINING',loadfactor=0.5,cmpfunction=getKeyFunction):
    return model.newMap(maptype=tipo,loadfactor=loadfactor,comparefunction=cmpfunction)

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def cargarByCriteria(moviesCatalog,criteria,data,cmpfunction=getKeyFunction,hashType='PROBING',loadfactor=0.5):
    moviesCatalog[criteria] = crearHash(hashType)
    productoras = {}
    #Este ciclo ingresa cada uno de los datos
    i = 0
    p = 0
    print("Organizando Archivos...")
    for element in data['elements']:
        if i%3290 == 0:
            print (" " + str(p) + "%" + " completado", end="\r")
            p+=1
    #Caso en el que solo se necesite una columna
        if element[criteria] not in productoras:
            value = model.crearCatalogo('ARRAY_LIST')
            model.agregarFinal(value,(element))
            productoras[element[criteria]] = value


            #Condición para separar los géneros por '|'
            if criteria == 'genres':
                generos = element[criteria].split('|')
                for genero in generos:
                    if genero not in productoras:
                        value = model.crearCatalogo('ARRAY_LIST')
                        model.agregarFinal(value,(element))
                        productoras[genero] = value
                    else:
                        model.agregarFinal(productoras[element[criteria]],element)

                
        else:
            model.agregarFinal(productoras[element[criteria]],element)
        i+=1

    #Agregar a la tabla de hash
    print("100%" +" completado\n")
    print("Creando y organizando un mapa...")
    i = 0
    p = 0
    for productora in productoras:
        if i%(round(len(productoras)/100)) == 0:
            print (" " + str(p) + "%" + " completado", end="\r")
            p+=1
        model.agregarAlMap(moviesCatalog[criteria],productora,productoras[productora])
        i+=1
    print ("100%" +" completado\n")

def cargarArchivosUnificados(details,casting, cmpfunction=None):
    lst=iniciarCatalogo()
    dialect = csv.excel()
    dialect.delimiter=";"
    i = 0
    p = 0
    print("Cargando archivos...")
    with open(cf.data_dir + details, encoding="utf-8-sig") as csvfile1:
        row = csv.DictReader(csvfile1, dialect=dialect)
        for elemento in row:
            if i%3290 == 0:
                print (" " + str(p) + "%" + " completado", end="\r")
                p+=1
            model.agregarFinal(lst,elemento)
            i+=1
    print ("100%" +" completado\n")
    print("Uniendo datos...")
    with open(cf.data_dir + casting, encoding="utf-8-sig") as csvfile2: #Cambiamos el encoding ya que generaba
        row = csv.DictReader(csvfile2,dialect=dialect)                  #un error con los archivos grandes
        i = 0
        p = 0
        for elemento in row:
            if i%3290 == 0:
                print (" " + str(p) + "%" + " completado", end="\r")
                p+=1
            if elemento["id"] == model.buscarPeliculas(lst,i)["id"]:
                for column in elemento:
                    if column != "id":
                        model.buscarPeliculas(lst,i)[column] = elemento[column]
            i += 1
    print ("100%" +" completado\n")
    return lst

def getParejaKV(mapa,key):
    return model.buscarKeyMap(mapa,key)

def limpiarProductora(mapa,key):
    peliculas = getParejaKV(mapa,key)
    peliculas_lista = model.crearCatalogo()
    suma = 0
    for pelicula in peliculas['value']['elements']:
        model.agregarFinal(peliculas_lista,(pelicula['title'],pelicula['vote_average']))
        suma += float(pelicula['vote_average'])
    size = model.tamanio(peliculas_lista)
    if size != 0:
        return (peliculas_lista,size, suma/size)
    return (peliculas_lista,0,0)

def limpiarGeneros(mapa,key):
    peliculas = getParejaKV(mapa,key)
    peliculas_lista = model.crearCatalogo()
    suma = 0
    for pelicula in peliculas['value']['elements']:
        model.agregarFinal(peliculas_lista,(pelicula['title'],pelicula['vote_count'],pelicula['genres']))
        suma += float(pelicula['vote_count'])
    size = model.tamanio(peliculas_lista)
    if size != 0:
        return (peliculas_lista,size, suma/size)
    return (peliculas_lista,0,0)