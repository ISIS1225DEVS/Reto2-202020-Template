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

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    
    catalog = {"Movies": None,
                "ProdCompanies": None,
                "AvgVote": None,
                "Directors": None,
                "Actors": None,
                "Genres": None,
                "VoteCounts": None,
                "ProdCountries": None,
                "Dates": None}
    
    catalog["Movies"] = lt.newList("SINGLE_LINKED", compareBookIds)
    catalog["ProdCompanies"] = mp.newMap(1000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareProdCompanies)
    catalog["AvgVote"] = mp.newMap(1000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareAvgVotes)
    catalog["Directors"] = mp.newMap(1000,
                                maptype="PROBING",
                                loadfactor=0.4,
                                comparefunction=compareDirectors)
    catalog["Actors"] = mp.newMap(1000,
                                    maptype="PROBING"
                                    loadfactor=0.4,
                                    comparefunction=compareActors)
    catalog["Genres"] = mp.newMap(1000,
                                    maptype="PROBING",
                                    loadfactor=0.4,
                                    comparefunction=compareGenres)
    catalog["VoteCounts"] = mp.newMap(1000,
                                    maptype="PROBING",
                                    loadfactor=0,4,
                                    comparefunction=compareVoteCounts)
    catalog["ProdCountries"] = mp.newMap(1000,
                                        maptype="PROBING",
                                        loadfactor=0.4,
                                        comparefunction=compareCountries)
    catalog["Dates"] = mp.newMap(1000,
                                maptype="PROBING",
                                loadfactor=0.4,
                                comparefunction=compareDates)
    
    return catalog
# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


