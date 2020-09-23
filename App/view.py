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
import controller as cont

import csv

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________





# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def main():
    a=False
    while a==False:
        print("""Seleccione opcion:
        1 Cargar archivo
        2 Buscar director
        3 Buscar genero
        4 Buscar Compañia""")
        
        opcion=int(input("Ingrese opcion"))
        if opcion==1:
            catalogo=cont.initpeliculas()
            archivo1=cont.loadMovies()
            archivo2=cont.loadMovies2()
            mapa_directores=cont.cargar_directores(catalogo,archivo1,archivo2)
            mapa_generos=cont.cargar_generos(catalogo,archivo1,archivo2)
            mapa_compañias=cont.cargar_compañias(catalogo,archivo1)
        elif opcion==2:
            nombre=input("Ingrese director")
            lista=cont.buscar_director(mapa_directores,nombre)
            print("Cantidad de peliculas",lt.size(lista["value"]))
            print(lista)
        elif opcion==3:
            genero=input("Ingrese genero")
            lista=cont.buscar_genero(mapa_generos,genero)
            print("Cantidad de peliculas",lt.size(lista["value"]))
            print(lista)
        elif opcion==4:
            compañia=input("Ingrese compañia")
            lista=cont.buscar_compañia(mapa_compañias,compañia)
            print("Cantidad de peliculas",lt.size(lista["value"]))
            print(lista)
     
main()
