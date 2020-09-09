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

details = "Data/SmallMoviesDetailsCleaned.csv"

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printMovieData(element):
    print(element["title"]+":")
    print("a. Fecha de estreno: "+element["release_date"])
    print("b. Promedio de la votación: "+element["vote_average"])
    print("c. Número de votos: "+element["vote_count"])
    print("d. Idioma: "+element["original_language"]+"\n")

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Iniciar lista")
    print("2- Cargar peliculas a la lista lista")
    print("0- Salir")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Iniciando lista ....")
        lista = controller.iniciarLista()
        print("Se creo lista con exito")
    elif int(inputs[0]) == 2:
        print("Cargando películas ....")
        size,first,last = controller.cargarPeliculas(lista, details)
        print("Se cargaron "+str(size)+ " películas"+"\n")
        printMovieData(first)
        printMovieData(last)
    else:
        sys.exit(0)
sys.exit(0)
