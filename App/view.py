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
#detalles = "AllMoviesDetailsCleaned.csv"
#casting = "AllMoviesCastingRaw.csv"
detalles = "SmallMoviesDetailsCleaned.csv"
casting = "MoviesCastingRaw-small.csv"


#___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def imprimirPeliculasPais(paises):
    print('Se encontraron: ' + str(lt.size(paises)) + ' peliculas')
    iterator = it.newIterator(paises)
    while it.hasNext(iterator):
        pelicula = it.next(iterator)
        print(pelicula)
        print("--------------------")

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- (Req-1)Consultar peliculas por compañia")
    print("4- (Req-2)Consultar peliculas por director")
    print("5- (Req-3)Consular peliculas por actor")
    print("6- (Req-4)Consultar peliculas por genero")
    print("7- (Req-5)Consultar peliculas por pais")


catalogo = None
Altair = True
while Altair == True:
    printMenu()
    Monika = input('Seleccione una opción para continuar\n')
    if int(Monika) == 1:
        catalogo = controller.iniciar_catalogo()
        print("Catalogo creado exitosamente")
    elif int(Monika) == 2:
        t1 = process_time()
        controller.cargar_info(catalogo, detalles, casting)
        print(lt.size(catalogo["archivo_peliculas"]))
        t2 = process_time()
        
        print("tiempo de procesado", t2-t1,"segundos")
    elif int(Monika) == 3:
        sara = input("Nombre de la compañia: ")
        t1 = process_time()
        print(controller.mostrar_compañias(catalogo, sara))
        t2 = process_time()
        print("tiempo de procesado", t2-t1,"segundos")
    elif int(Monika)== 4:
        monika = input("Nombre del director: ")
        t1 = process_time()
        print(controller.mostrar_directores(catalogo, monika))
        t2 = process_time()
        print("tiempo de procesado", t2-t1,"segundos")
    elif int(Monika)== 5:
        monika = input("Nombre del actor: ")
        t1 = process_time()
        print(controller.mostrar_actor(catalogo, monika))
        t2 = process_time()
        print("tiempo de procesado", t2-t1,"segundos")
    elif int(Monika)== 6:
        monika = input("Genero que desea buscar: ")
        t1 = process_time()
        print(controller.mostrar_generos(catalogo, monika))
        t2 = process_time()
        print("tiempo de procesado", t2-t1,"segundos")
    elif int(Monika)== 7:
        monika = input("Pais que desea buscar: ")
        t1 = process_time()
        paises = controller.mostrar_pais(catalogo, monika)
        t2 = process_time()
        imprimirPeliculasPais(paises)
        print("tiempo de procesado", t2-t1,"segundos")
    else:
        Altair = False
