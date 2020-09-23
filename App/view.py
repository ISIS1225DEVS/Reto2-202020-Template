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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
from time import process_time
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
file1 = "MoviesCastingRaw-small.csv"
file2 = "SmallMoviesDetailsCleaned.csv"

#file1 = "AllMoviesCastingRaw.csv"
#file2 = "AllMoviesDetailsCleaned.csv"




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def imprimirProductoras(result):
    print("\nPelículas de:",productora)
    iterator = it.newIterator(result[0])
    while it.hasNext(iterator):
        pelicula = it.next(iterator)
        print("{:<50}{:<50}".format(pelicula[0],pelicula[1]))
    print("\nLa cantidad de películas de la productora es:",result[1])
    print("El promedio de las películas de la productora es:",round(result[2],2))

def imprimirGeneros(result):
    print("\nPelículas de:",genero)
    iterator = it.newIterator(result[0])
    while it.hasNext(iterator):
        pelicula = it.next(iterator)
        print("{:<50}{:<5}{:<10}".format(pelicula[0],pelicula[1],pelicula[2]))
    print("\nLa cantidad de películas del género es:",result[1])
    print("El promedio de la cantidad de votos del género es:",round(result[2],2))

def imprimirActores(result):
    print("\nPelículas de:",actor)
    iterator = it.newIterator(result[0])
    while it.hasNext(iterator):
        pelicula = it.next(iterator)
        print("{:<50}{:<5}{:<10}".format(pelicula[0],pelicula[1],pelicula[2]))
    print("\nLa cantidad de películas del actor es:",result[1])
    print("El promedio de la cantidad de votos de las películas del actor:",round(result[2],2))
    print("El nombre del director con el que mas ha colaborado es:", result[3])    
# ___________________________________________________
#  Menu principal
# ___________________________________________________
def imprimirMenu():
    print("\n1- Inicializar Catálogo")
    print("2- Cargar Datos")
    print("3- Descubrir productoras de cine")
    print("4- Conocer a un director")
    print("5- Conocer a un actor")
    print("6- Entender un género cinematográfico")
    print("7- Encontrar películas por país")
    print("0- Salir\n")


data = None
moviesCatalog = {}
while True:
    imprimirMenu()
    seleccion = input("Seleccione una opción\n")
    if int(seleccion[0]) == 1:
        t1 = process_time()
        data = controller.cargarArchivosUnificados(file2,file1)
        t2 = process_time()
        print("Tiempo de ejecución (sin contar los prints):",t2-t1,"Segundos")
    elif int(seleccion[0]) == 2:
        if data != None:
            t1 = process_time()
            print("Cargando productoras:")
            controller.cargarByCriteria(moviesCatalog,"production_companies",data) # Aquí se escribe el factor de carga loadFactor, el tipo de tabla hashType, y la función de comparación 
            print("Cargando generos:")
            controller.cargarByCriteria(moviesCatalog,"genres",data)
            t2 = process_time()
            print("Tiempo de ejecución:",t2-t1,"Segundos")
        else:
            print("\nPor favor inicialice el catálogo primero")

    elif int(seleccion[0]) == 3:
        if data != None and moviesCatalog != {}:
            productora = input("Por favor ingrese el nombre de la productora que consultar:\n")
            t1 = process_time()
            result = controller.limpiarProductora(moviesCatalog["production_companies"],productora)
            # print(result)
            t2 = process_time()
            imprimirProductoras(result)
            print("Tiempo de ejecución:",t2-t1,"Segundos")
        else:
            print("\nPor favor inicialice el catálogo o cargue los datos primero")
    elif int(seleccion[0]) == 4:
        pass
    elif int(seleccion[0]) == 5:
        actor = input("Por favor ingrese el nombre del actor que desea consultar:\n")
        t1 = process_time()
        controller.cargarByPerson(moviesCatalog,"actor",data,actor)
        result = controller.limpiarPersona(moviesCatalog[actor],actor)
        t2 = process_time()
        imprimirActores(result)
        print("Tiempo de ejecución:",t2-t1,"Segundos")
    elif int(seleccion[0]) == 6:
        genero = input("Por favor ingrese el nombre del género cinematográfico que desea consultar:\n")
        t1 = process_time()
        result = controller.limpiarGeneros(moviesCatalog["genres"],genero)
        t2 = process_time()
        imprimirGeneros(result)
        print("Tiempo de ejecución (sin contar los prints):",t2-t1,"Segundos")
    elif int(seleccion[0]) == 7:
        pass
    elif int(seleccion[0]) == 0:
        sys.exit()
    else:
        print("Por favor ingrese una opción válida")
