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
import model as mod


import config as cf
import sys
import csv


from time import process_time 


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

    archivo={"size":0}
    tablacompanies={"size":0}
    while True:
        
        print("Seleccione opcion:\n1) Cargar archivo\n2) requerimiento 1")
        opcion=int(input("Ingrese opcion\n"))
        if opcion==1:
            nombre=input("Inserte nombre del archivo a cargar\n")
            archivo=cont.cargar_archivo("Data/"+nombre)
            tablacompanies=cont.tablahash(archivo,"production_companies")
            print("Datos cargados, ",archivo['size']," elementos cargados")
            if archivo['size']>0:
                print(lt.getElement(archivo,1))
                print(lt.lastElement(archivo))
                
            else:
                print("Archivo vacío")
        elif opcion==2:
            company=input("ingrese el nombre de la compañia interesada\n")
            dato=cont.buscar(tablacompanies,company)
            print(dato)
            
        else:
            sys.exit(0)



main()

    print("""Seleccione opcion:
    1 Cargar archivo""")
    opcion=int(input("Ingrese opcion"))
    if opcion==1:

        archivo1=cont.loadMovies()
        catalogo=cont.initpeliculas()
        mapa=cont.cargar_datos(catalogo,archivo1)
        return mapa

main()

        nombre=input("Inserte nombre del archivo a cargar")
        catalogo=cont.initpeliculas()
        lista=cont.cargar_datos(catalogo,nombre)
        print(lista)
main()

