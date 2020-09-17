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

import config as cf
import sys
import csv

from time import process_time 


"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def loadCSVFile (file, sep=";"):
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    return lst

# Funciones para agregar informacion al catalogo

def comparecompanies(c1, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (c1 == identry):
        return 0
    elif (c1 >identry):
        return 1
    else:
        return -1
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------



def tablahash(lista,criteria):
    llaves={}
    
    for i in range(1,lt.size(lista)):
        a=lt.getElement(lista,i)
        if a[criteria] not in llaves.keys():
            b=lt.newList("ARRAY_LIST",None)
            lt.addFirst(b,a["original_title"])
            llaves[a[criteria]]=[b,float(a["vote_average"]),1]
        else:
            lt.addLast(llaves[a[criteria]][0],a["original_title"])
            llaves[a[criteria]][1]+=float(a["vote_average"])
            llaves[a[criteria]][2]+=1
    q=mp.newMap(numelements=len(llaves.keys()), prime=109345121, maptype='CHAINING', loadfactor=0.5,comparefunction=comparecompanies)
    for x in llaves.keys():
        llaves[x][1]=llaves[x][1]/llaves[x][2]
        lt.addLast(llaves[x][0],("promedio:",llaves[x][1]))
        lt.addLast(llaves[x][0],("cantidad: ",llaves[x][2]))
        llaves[x].remove(llaves[x][2])
        llaves[x].remove(llaves[x][1])
        a=llaves[x]
        mp.put(q,x,a)
    return q
            

  
def buscar(lista,company):
    a=mp.get(lista,company)
    return(me.getValue(a)) 


# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones de Comparacion
# ==============================
