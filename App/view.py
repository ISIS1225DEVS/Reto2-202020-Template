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
        2 Buscar productora
        3 Buscar director
        4 Buscar actor
        5 buscar genero
        6 buscar pais""")
        
        opcion=int(input("Ingrese opcion\n"))
        if opcion==1:
            catalogo=cont.initpeliculas()
            archivo1=cont.loadMovies()
            archivo2=cont.loadMovies2()
            mapa_actores=cont.cargar_actores(catalogo,archivo1,archivo2)
            mapa_directores=cont.cargar_directores(catalogo,archivo1,archivo2)
            mapa_generos=cont.cargar_generos(catalogo,archivo1,archivo2)
            mapa_compañias=cont.cargar_compañias(catalogo,archivo1)
            mapa_pais=cont.cargar_pais(catalogo,archivo1,archivo2)
            
        elif opcion==3:
            nombre=input("Ingrese director\n")
            lista=cont.buscar_director(mapa_directores,nombre)
            print("Cantidad de peliculas:",lt.size(lista["lista"]["value"]))
            print(lista)
        elif opcion==5:
            genero=input("Ingrese genero\n")
            lista=cont.buscar_genero(mapa_generos,genero,catalogo["genres_vote"])
            print("Cantidad de peliculas:",lt.size(lista["lista"]["value"]))
            print(lista)
        elif opcion==2:
            compañia=input("Ingrese compañia\n")
            lista=cont.buscar_compañia(mapa_compañias,compañia)
            print("Cantidad de peliculas:",lt.size(lista["lista"]["value"]))
            print(lista)
        elif opcion==4:
            actor=input("ingrese nombre del actor\n")
            lista=cont.buscar_actores(mapa_actores,actor)
            print("cantidad de peliculas:",lt.size(lista["lista"]["value"]))
            print(lista)
        elif opcion==6:
            pais=input("ingrese el nombre del pais de interes\n")
            lista=cont.buscar_pais(mapa_pais,pais)
            
            print(lista)


     
main()
