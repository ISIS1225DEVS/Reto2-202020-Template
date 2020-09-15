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
import model as mdl
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt

import config as cf
import sys
import csv


from time import process_time 

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


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def initpeliculas():
    catalogo=mdl.nuevos_mapas
    return catalogo

def cargar_datos(catalogo,archivo):
    peliculas=mdl.loadCSVFile(archivo, sep=";")
    for elemento in range(1,lt.size(peliculas)):
        actual=lt.getElement(peliculas,elemento)
        nuevo=mdl.cargar_compañias(catalogo,peliculas["production_companies"],(peliculas["production_companies"],peliculas["title"]))
    return nuevo
        