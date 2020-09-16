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

def loadCSVFile2 (file, sep=";"):
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
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
    peliculas={"id":None,"budget":None,"genres":None,"imdb_id":None,"original_language":None,"original_title":None,
    "overview":None,"popularity":None,"production_companies":None,"production_countries":None,"release_date":None,"spoken_languages":None,"status":None,"tagline":None,"title":None,"vote_average":None,"vote_count":None,
    "production_companies_number":None,"production_countries_number":None,"spoken_languages_number":None}

    peliculas["production_companies"]=mp.newMap(2003,2011,maptype='CHAINING',loadfactor=0.9,comparefunction=None)
    return peliculas

def cargar_compañias(catalogo,compañia,valor):
    nuevo_catalogo=mp.put(catalogo,compañia,valor)
    return nuevo_catalogo


# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


