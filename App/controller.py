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
def iniciar_catalogo():
    catalogo = model.catalogo()
    return catalogo




# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def cargar_info(catalogo, archivo1, archivo2):
    cargar_datos(catalogo, archivo1)
    cargar_casting(catalogo, archivo2)
    
    




def cargar_datos(catalogo, archivo):
    sep = ";"
    dialect = csv.excel()
    dialect.delimiter=sep
    archivo = cf.data_dir + archivo
    input_file = csv.DictReader(open(archivo, encoding="utf-8"), dialect=dialect)
    
    for movie in input_file:
        model.addmovie(catalogo, movie)
        compañia = movie["production_companies"] # Se obtienen las compañias
        generos = (movie["genres"]).split(sep="|")
        model.añadir_compañia(catalogo, movie, compañia)
        model.añadir_genero(catalogo, movie, generos)

def cargar_casting(catalogo, archivo):
    sep = ";"
    dialect = csv.excel()
    dialect.delimiter=sep
    archivo = cf.data_dir + archivo
    input_file = csv.DictReader(open(archivo, encoding="utf-8"), dialect=dialect)

    for movie in input_file:
        director = movie["director_name"]
        model.añadir_director(catalogo, movie, director)
        model.añadir_actor(catalogo, movie)



def mostrar_compañias(catalogo, sara):
    N = model.mostrar_compañias(catalogo, sara)
    if N != "No existe esa compañia en la base de datos":
        C = model.calificacion(N)
        return [C, N]
    else:
        return N

def mostrar_directores(catalogo, Monika):
    N = model.mostrar_director(catalogo, Monika)
    if N != "No existe ese autor en la base de datos":
        C = model.calificacion2(N)
        return [C, N]
    else:
        return N

def mostrar_generos(catalogo, Misaka):
    N = model.mostrar_generos(catalogo, Misaka)
    if N != "No existe ese genero en la base de datos":
        C = model.calificacion(N)
        return [C, N]
    else:
        return N

def mostrar_actor(catalogo, Misaka):
    N = model.mostrar_actores(catalogo, Misaka)
    if N != "No existe ese actor en la base de datos":
        C = model.calificacionActor(N)
        return [C, N]
    else:
        return N


A = ("A mario lacerna le gusta la papaya").strip()
print(A)


