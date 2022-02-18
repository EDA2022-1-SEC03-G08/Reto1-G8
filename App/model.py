"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
from optparse import TitledHelpFormatter
from platform import release
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from datetime import datetime as dt
assert cf


"""
Se define la estructura de un catálogo de Spotify.
El catálogo tendrá tres listas, una para los albumes, otra para las artistas
y otra para las canciones.
"""


# Construccion de modelos
def newCatalog():

    catalog = {"albums": None,
               "artist": None,
               "tracks": None}

    catalog["albums"] = lt.newList('ARRAY_LIST', cmpfunction=compareAlbums)
    catalog["artist"] = lt.newList('ARRAY_LIST')
    catalog["tracks"] = lt.newList('ARRAY_LIST')

    return catalog


# Funciones para agregar informacion al catalogo
def addAlbum(catalog, albumdic):
    neoAlbum = newAlbum(albumdic)
    lt.addLast(catalog['albums'], neoAlbum)
    return catalog

# Funciones para creacion de datos


def newAlbum(albumdic):
    if albumdic["release_date"].startswith(("Jan", "Feb", "Mar", "Apr",
                                            "May", "Jun", "Jul", "Aug",
                                            "Sep", "Oct", "Nov", "Dec")):

        date_format = dt.strptime(albumdic["release_date"], "%b-%y")
        anio = int(dt.strftime(date_format, "%Y"))

    else:
        try:
            date_format = dt.strptime(albumdic["release_date"], "%Y-%m-%d")
            anio = int(dt.strftime(date_format, "%Y"))

        except ValueError:
            date_format = dt.strptime(albumdic["release_date"], "%Y")
            anio = int(dt.strftime(date_format, "%Y"))

    albumdic["release_date"] = anio
    return albumdic
# Funciones de consulta

# FUnciones de inidcadores de tamaño


def albumSize(catalog):
    return lt.size(catalog['albums'])


def artistSize(catalog):
    return lt.size(catalog['artist'])


def trackSize(catalog):
    return lt.size(catalog['tracks'])


# Funciones utilizadas para comparar elementos dentro de una lista
def compareAlbums(album1, album2):
    return album1["release_date"] < album2["release_date"]
# Funciones de ordenamiento


def sortAlbums(catalog):
    sa.sort(catalog['albums'], compareAlbums)
