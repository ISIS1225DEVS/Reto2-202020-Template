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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
def catalogo():
    catalogo = {"archivo_peliculas": None,
                "peliculas_por_compañia": None}


    catalogo["peliculas_por_compañia"] = mp.newMap( numelements=10003,
                                                    prime=109345121,   
                                                    maptype='CHAINING', 
                                                    loadfactor=0.5, 
                                                    comparefunction=companiescomparer)
                                                 
    catalogo["archivo_peliculas"] = lt.newList("ARRAY_LIST")
    return catalogo
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------



# Funciones para agregar informacion al catalogo
def añadir_compañia(catalogo, movie, compañia):
    if mp.contains(catalogo["peliculas_por_compañia"], compañia) == True:
        lt.addLast(me.getValue(mp.get(catalogo["peliculas_por_compañia"], compañia)), movie["original_title"])
    else:
        N = lt.newList("ARRAY_LIST")
        lt.addLast(N, movie["original_title"])
        mp.put(catalogo["peliculas_por_compañia"], compañia, N)


def addmovie(catalogo, movie):

    lt.addLast(catalogo["archivo_peliculas"], movie)





# ==============================
# Funciones de consulta
# ==============================
def mostrar_compañias(catalog):
    A = mp.keySet(catalog["peliculas_por_compañia"])
    return A

# ==============================
# Funciones de Comparacion
# ==============================
def companiescomparer(keyname, compani):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    comp_entry = me.getKey(compani)
    if (keyname == comp_entry):
        return 0
    elif (keyname > comp_entry):
        return 1
    else:
        return -1
