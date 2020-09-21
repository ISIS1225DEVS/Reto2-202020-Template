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
def cargarByCriteria(moviesCatalog,criteria,details,casting,cmpfunction=getKeyFunction,hashType='PROBING',loadfactor=0.5):
    data = cargarArchivosUnificados(details,casting,cmpfunction)
    moviesCatalog[criteria] = crearHash(hashType)
    productoras = {}
    for element in data['elements']:
        if element[criteria] not in productoras:
            value = model.crearCatalogo('ARRAY_LIST')
            model.agregarFinal(value,(element))
            productoras[element[criteria]] = value
        else:
            model.agregarFinal(productoras[element[criteria]],element)
    for productora in productoras:
        model.agregarAlMap(moviesCatalog[criteria],productora,productoras[productora])
    # return moviesCatalog            

def cargarArchivosUnificados(details,casting, cmpfunction=None):
    lst=iniciarCatalogo()
    dialect = csv.excel()
    dialect.delimiter=";"
    # try:
    with open(cf.data_dir + details, encoding="utf-8-sig") as csvfile1:
        row = csv.DictReader(csvfile1, dialect=dialect)
        for elemento in row:
            model.agregarFinal(lst,elemento)
    with open(cf.data_dir + casting, encoding="utf-8-sig") as csvfile2: #Cambiamos el encoding ya que generaba
        row = csv.DictReader(csvfile2,dialect=dialect)                  #un error con los archivos grandes
        i = 1
        for elemento in row:
            if elemento["id"] == model.buscarPeliculas(lst,i)["id"]:
                for column in elemento:
                    if column != "id":
                        model.buscarPeliculas(lst,i)[column] = elemento[column]
            i += 1
    # except:
        # print("Hubo un error con la carga del archivo")
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
