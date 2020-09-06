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

def loadData(catalog, DetailsFile, CastingFile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadDetails(catalog, DetailsFile)
    loadCasting(catalog, CastingFile)

def loadDetails(catalog, detailsfile):
    """
    Carga cada una de las lineas del archivo de libros.
    - Se agrega cada libro al catalogo de libros
    - Por cada libro se encuentran sus autores y por cada
      autor, se crea una lista con sus libros
    """
    detailsfile = cf.data_dir + detailsfile
    input_file = csv.DictReader(open(detailsfile))
    for movie in input_file:
        model.addMovie(catalog, movie)

        companie = movie["production_companies"] #Se obtienen las compañias
        model.addMovieCompanie(catalog, companie.strip(), movie)

        country = movie["production_countries"] # se obtienen los paises
        model.addMovieCountry(catalog, country.strip(), movie)

        genres = movie["genres"].split("|")
        for genre in genres:
            model.addMovieGenre(catalog, genre.strip(), movie)

def loadCasting(catalog, castingfile):


    castingfile = cf.data_dir + castingfile
    input_file = csv.DictReader(open(castingfile))
    for movie in input_file:
        model.addCasting(catalog, movie)

        actors = [movie["actor1_name"],movie["actor2_name"],movie["actor3_name"],movie["actor4_name"],movie["actor5_name"]]
        for actor in actors:
            model.addCastingActor(catalog,actor.strip(), movie)
        
        director = movie["director_name"]
        model.addCastingDirector(catalog,director.strip(), movie)


    