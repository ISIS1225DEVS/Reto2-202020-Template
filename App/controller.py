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

def loadDataMovies(catalog,moviesDetails,moviesCasting):
    loadMovieDetails(catalog, moviesDetails)
    loadMoviesCasting(catalog, moviesCasting)

def loadMovieDetails(catalog, moviesDetails):
    moviesDetails=cf.data_dir + moviesDetails
    input_file = csv.DictReader(open(moviesDetails))
    for movie in input_file:
        model.addMovie(catalog, movie)

def loadMoviesCasting(catalog, moviesCasting):
    moviesCasting=cf.data_dir + moviesCasting
    input_file = csv.DictReader(open(moviesCasting))
    for director in input_file:
        model.addMovie(catalog, director)




def moviesSize(catalog):
    return model.moviesSize(catalog)

def directorsSize(catalog):
    return model.directorsSize(catalog)

def actorsSize(catalog):
    return model.actorsSize(catalog)

def getMoviesbyDirector(catalog, directorname):
    directorinfo = model.getMoviesByDirector(catalog, directorname)
    return directorinfo

        
        
