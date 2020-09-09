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




# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def newListDetails():
    a = model.newList()
    return a

def loadDetails(lst, detailsfile):
    detailsfile = cf.data_dir + detailsfile
    dialect = csv.excel()
    dialect.delimiter = ";"
    input_file = csv.DictReader(open(detailsfile,encoding="utf-8"),dialect= dialect)
    for movie in input_file:
        model.addLast(lst,movie)

def detailsSize(lst):
    size = model.giveSize(lst)
    return size

def getFirstElement(lst):
    first_element=model.getFirstElement(lst)
    return first_element

def getLastElement(lst):
    last_element=model.getLastElement(lst)
    return last_element

def getTitle(element):
    title=model.getTitle(element)
    return title

def getDate(element):
    date=model.getDate(element)
    return date

def getAverage(element):
    average=model.getAverage(element)
    return average

def getVotes(element):
    votes=model.getVotes(element)
    return votes

def getLang(element):
    lang=model.getLang(element)
    return lang
