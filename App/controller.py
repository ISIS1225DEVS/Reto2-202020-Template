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
from App import model as model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    catalog = model.newCatalog()
    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadData(catalog, detailsfile, castingfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    dialect = csv.excel()
    dialect.delimiter = ";"
    detailsfile = cf.data_dir + detailsfile
    #input_file = #csv.DictReader(open(detailsfile,encoding="utf-8"), dialect=dialect)
    input_file = csv.DictReader(open(detailsfile,encoding="utf-8"),dialect= dialect)
    castingfile = cf.data_dir + castingfile
    input_file2 = csv.DictReader(open(castingfile,encoding="utf-8"),dialect= dialect)

    for movie in input_file:
      model.addMovie(catalog,movie)
    for casting in input_file2:
      model.addCasting(catalog,casting)



# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def movieSize(catalog):
    size = model.moviesSize(catalog)
    return size

def moviesByCompany(catalog, company):
    info = model.getMoviesByCompany(catalog,company)
    movies = info[0]
    count = model.listSize(movies)
    moviesReduced = model.getFifteenElements(movies)
    prom = info[1]/count
    return (moviesReduced, count, prom)

def moviesByGenre(catalog,genre):
  info = model.getMoviesByGenre(catalog, genre)
  movies = info[0]
  count = model.listSize(movies)
  moviesReduced = model.getFifteenElements(movies)
  prom = info[1]/count
  return (moviesReduced,count,prom)