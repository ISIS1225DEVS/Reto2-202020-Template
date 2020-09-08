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
allmovies = 'Movies/AllMoviesCastingRaw.csv'
detailmovies = 'Movies/AllMoviesDetailsCleaned.csv'
castingmovies = 'Movies/MoviesCastingRaw-small.csv'
smallmovies = 'Movies/SmallMoviesDetailsCleaned.csv'
# ___________________________________________________ 
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Cargar informacion del catalogo")
    print("2- Mombres y cantidad de peliculas por productora")
    print("3- Trabajos de un director")
    print("4- Trabajos de un actor")
    print("5- Peliculas por genero cinematografico")
    print("6- Peliculas por pais")
    print("0- Salir")


while True:
    print_menu()
    inputs = input('Seleccione una opción para continuar')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos...")
        controller.loadData(cont, allmovies, detailmovies, castingmovies, smallmovies)
        print('Peliculas cargadas: ' + str(controller.detailmovies(cont)))
        print('Actores cargados: ' + str(controller.castingmovies(cont)))
    elif int(inputs[0]) == 2:
        None
    elif int(inputs[0]) == 3:
        None
    elif int(inputs[0]) == 4:
        None
    elif int(inputs[0]) == 5:
        None
    elif int(inputs[0]) == 6:
        None
    elif int(inputs[0]) == 0:
        sys.exit(0)
sys.exit(0)
 