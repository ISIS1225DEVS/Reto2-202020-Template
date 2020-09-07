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
file1 = "MoviesCastingRaw-small.csv"
file2 = "SmallMoviesDetailsCleaned.csv"




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
while True:
    imprimirMenu()
    listaMovies = controller.iniciarCatalogo('ARRAY_LIST')
    seleccion = input("Seleccione una opción\n")
    if int(seleccion[0]) == 1:
        print("Cargando archivos...")
        listaMovies = controller.cargarArchivos(file1,file2)
        print("Se cargaron",listaMovies["size"],"películas\n")
        el_in = lt.getElement(listaMovies,1)
        el_fin = lt.getElement(listaMovies,0)
        print("{:<21}{:<21}{:<21}{:<21}{:<21}".format("Título","Fecha de estreno","Votación promedio","Cantidad de votos","Idioma"))
        print("{:<21}{:<21}{:<21}{:<21}{:<21}".format(el_in["title"],el_in["release_date"],el_in["vote_average"],el_in["vote_count"],el_in["spoken_languages"]))
        print("{:<21}{:<21}{:<21}{:<21}{:<21}".format(el_fin["title"],el_fin["release_date"],el_fin["vote_average"],el_fin["vote_count"],el_fin["spoken_languages"]))
    elif int(seleccion[0]) == 2:
        pass
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
    