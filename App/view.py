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

moviesfile = 'Data/Peliculas/SmallMoviesDetailsCleaned.csv'
castingfile = 'Data/Peliculas/MoviesCastingRaw-Small.csv'

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printmenu():
    print('Bienvenido')
    print('1. Cargas Archivos')
    print('0. Salir del programa')


"""
 Menú principal
"""
while True:
    printmenu()
    inputs = input('Seleccione una opción para continuar: \n')
    
    if int(inputs[0]) == 1:
        print('Inicializando Catálogo....')
        cont = controller.initCatalog_movies()
        controller.loadData(cont, moviesfile)
        print('Se cargaron ',controller.movies_size(cont), 'datos')
        title1, date1, average1, number1, language1 = controller.movies_data(cont,1)
        title2, date2, average2, number2, language2 = controller.movies_data(cont,controller.movies_size(cont))
        print('La primera película del catálogo es', title1, 'fue estrenada el ', date1, ', tuvo un promedio de votación de ', average1, ' con un número de votos de', number1, 'y su idioma original fue ', language1)
        print('La última película del catálogo es', title2, 'fue estrenada el ', date2, ', tuvo un promedio de votación de ', average2, ' con un número de votos de', number2, 'y su idioma original fue ', language2)
        
    elif int(inputs[0]) == 0:
        sys.exit(0)
sys.exit(0)



