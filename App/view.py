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

moviedb = 'Data/themoviesdb/MoviesDetailsCleaned-large.csv' 
actorsdb = 'themoviesdb/MoviesCastingRaw-small.csv'

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("\n********************************  Grupo 04  ******************************************")
    print("\n*********** CONSOLA DEL RETO 2 @@@ EXPLORANDO LA MAGIA DEL CINE RECARGADO @@@  *******")
    print("\n**************************************************************************************")
    print(" ")
    print("(1) Inicializar y cargar catálogo de movies")
    print("(2) Imprimir  primera y última pelicua del catálogo de movies")
    print("(3)   placeholder - REQ. 1: Consultar los productoras de cine")
    print("(4)   placeholder - REQ. 2: Consultar los a un director")
    print("(5)   placeholder - REQ. 3: Consultar a un actor")
    print("(6)   placeholder - REQ. 4: Entender un genero cinematografico")
    print("(7)   placeholder - REQ. 5: Consultar peliculas por pais")
    print("(0) Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    

    #se reemplazo la separación entre casting s y casting L. Es redundante caragr ambos metodos
    if int(inputs[0]) == 1:

        resultList= controller.loadMovies(moviedb, compareRecordIds)
        
        print('Se cargaron: ', lt.size(resultList), ' peliculas')

    elif int(inputs[0]) == 2:
        primera = (lt.getElement(resultList,1))
        ultima = (lt.getElement(resultList, (int(lt.size(resultList)))))
        
        print ("se encontraron :", lt.size(resultList), " peliculas" )  
        print((0, (lt.getElement(resultList,1))['original_title']))         
        print("primera pelicula: ", (primera['original_title']), (primera['original_language']), (primera['release_date']), (primera['vote_count']), (primera['vote_average']) )
        print("ultima pelicula: ", (ultima['original_title']), (ultima['original_language']), (ultima['release_date']), (ultima['vote_count']), (ultima['vote_average']) )
        input ("presione una tecla para volver al menu...")
        

        
    elif int(inputs[0]) == 3:
        pass    

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass
    else:
        sys.exit(0)
sys.exit(0)