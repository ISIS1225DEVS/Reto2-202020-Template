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
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Conocer una productora")
    print("4- Conocer un genero")
    print("0- Salir")


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog=controller.iniciarcatalog()
        print("Se ha inicializado el catalogo...")
    
    elif int(inputs[0])==2:
        print("Cargando información de los archivos ....")
        controller.loadDatos(catalog)
        print ('Peliculas cargados: ' + str(lt.size(catalog['Peliculas'])))
        print ('Directores cargados: ' + str(lt.size(catalog['Directores'])))
        print ('Géneros cargados: ' + str(lt.size(catalog['Generos'])))
        print("Productoras cargadas"+ str(lt.size(catalog["Productoras"]) ),"\n")

        pelicula1=lt.getElement(catalog["Peliculas"],1)
        pelicula2=lt.getElement(catalog["Peliculas"],lt.size(catalog["Peliculas"]))
        print("La primera pelicula es:\n",pelicula1,"\n\n","Titulada:",pelicula1["original_title"],"\n","Estrenada el dia:",pelicula1["release_date"])
        print(" Su promedio de votacion:",pelicula1["vote_average"],"\n","su numero de votos",pelicula1["vote_count"],"\n","Y su idioma:",pelicula1["original_language"],"\n")
        print("La ultima pelicula es:\n",pelicula2,"\n\n","Titulada:",pelicula2["original_title"],"\n","Estrenada el dia:",pelicula2["release_date"])
        print(" Su promedio de votacion:",pelicula2["vote_average"],"\n","su numero de votos",pelicula2["vote_count"],"\n","Y su idioma:",pelicula2["original_language"],"\n")
    
    elif int(inputs[0])==3:
        nombre=input("Ingrese el nombre de la productora:\n")
        productora= controller.darProductora(catalog,nombre)
        print(productora)
        print("La productora",nombre,"tiene",lt.size(productora["Peliculas"]),"peliculas las cuales son:\n")     
        iterador= it.newIterator(productora["Peliculas"])
        while it.hasNext(iterador):
            element=it.next(iterador)
            print(element,"\n")
            print("----------------------"*7,"\n")
            print("Con un promedio de votos de",productora["Vote_average"])
    
    elif int(inputs[0])==4:
        nombre=input("Ingrese el nombre del director:\n")
        director=controller.darDirector(catalog,nombre)
        print(director)

    else:
        sys.exit(0)
sys.exit(0)



# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
