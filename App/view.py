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
# file1 = "MoviesCastingRaw-small.csv"
# file2 = "SmallMoviesDetailsCleaned.csv"

file1 = "AllMoviesCastingRaw.csv"
file2 = "AllMoviesDetailsCleaned.csv"




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def imprimirMenu():
    print("\n1- Cargar Datos")
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer a un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("0- Salir\n")

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print('Bienvenid@')
    print('1- Cargar Películas')
    print('2- ')
    print('3- ')
    print('0- Salir')

while True:
    imprimirMenu()
    # listaMovies = controller.iniciarCatalogo('ARRAY_LIST')
    seleccion = input("Seleccione una opción\n")
    # try:
    if int(seleccion[0]) == 1:
        moviesCatalog = {}
        print("Cargando archivos...")
        t1 = process_time()
        moviesCatalog = controller.cargarByCriteria(moviesCatalog,"production_companies",file2,file1)
        t2 = process_time()
        print("Tiempo de ejecución:",t2-t1,"Segundos")

    elif int(seleccion[0]) == 2:
        productora = input("Por favor ingrese el nombre de la productora que consulta:\n")
        t1 = process_time()
        result = controller.limpiarProductora(moviesCatalog["production_companies"],productora)
        t2 = process_time()
        print("Tiempo de ejecución:",t2-t1,"Segundos")
        print("\nPelículas de:",productora)
        iterator = it.newIterator(result[0])
        while it.hasNext(iterator):
            pelicula = it.next(iterator)
            print("{:<50}{:<50}".format(pelicula[0],pelicula[1]))
        print("\nLa cantidad de películas de la productora es:",result[1])
        print("El promedio de las películas de la productora es:",round(result[2],2))
        
    elif int(seleccion[0]) == 3:
        pass
    elif int(seleccion[0]) == 4:
        pass
    elif int(seleccion[0]) == 5:
        pass
    elif int(seleccion[0]) == 6:
        pass
    else:
        sys.exit()
    # except:
        # print("hubo un error")
