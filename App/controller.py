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
from DISClib.ADT import list as lt
from time import process_time


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

def loadData(catalog, Moviesfile):
    loadDetails(catalog, Moviesfile)

def loadDetails(catalog, Moviesfile):

    dialect = csv.excel()
    dialect.delimiter=";"

    try:
        with open( Moviesfile, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                model.addDetails(catalog, row)
                companies = row['production_companies']
                
                model.addProductoraMovie(catalog, companies, row)  
                model.addGenreMovie(catalog, genres, row)           
    except:
        print("Hubo un error con la carga del archivo")
    
    return 0
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def companySize(catalog):
    resultado = model.companySize(catalog)
    return resultado


def moviesByProductionCompany(catalog, productoraname):
    productorainfo = model.moviesByProductionCompany(catalog, productoraname)
    return productorainfo

#def moviesByGenre(catalog, genre):
    #genre_info = model.moviesByGenre(catalog,genre)
    #return genre_info

def detailSize(catalog):
    resultado = model.detailSize(catalog)
    return resultado

def encontrarElemento(camino,posicion):
    resultado = model.encontrarElemento(camino,posicion)
    return resultado