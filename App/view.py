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
import config as conf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from App import controller
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
detalles = "Data\AllMoviesDetailsCleaned.csv"
casting = "Data\AllMoviesCastingRaw.csv"
#detalles = "Data\SmallMoviesDetailsCleaned.csv"
#casting = "Data\MoviesCastingRaw-small.csv"


#___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
catalog = None
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- (Req-1)Consultar peliculas por compañia")

while True:
    printMenu()
    Monika = input('Seleccione una opción para continuar\n')
    if int(Monika) == 1:
        print("Inicializando Catálogo ....")
        t1 = process_time()
        # cont es el controlador que se usará de acá en adelante
        catalog = controller.initCatalog(detalles, casting)
        t2 = process_time()
        print("Catalogo creado exitosamente")
        print("tiempo de ejecución:",t2-t1,"segundos")
        #print(catalog)

    elif int(Monika) == 2:
        print("Cargando información al catalogo...")
        t1 = process_time()
        controller.cargar_elementos_al_catalogo(catalog)
        t2 = process_time()
        print("Proceso finalizado")
        print("tiempo de carga:",t2-t1,"segundos")
        #print(mp.keySet(catalog["production_companies(map)"]))
        #print(mp.valueSet(catalog["production_companies(map)"]))
    
    elif int(Monika) == 3:
         B = input("Ingrese nombre de la compañia")
         print("leyendo archivos...")
         t1 = process_time()
         Lista = controller.lista_pel_per_companie(catalog, B)
         t2 = process_time()
         print(Lista)
         print("tiempo de carga:",t2-t1,"segundos")




       
