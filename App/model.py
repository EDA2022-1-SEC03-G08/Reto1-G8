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
    # No se neceistan listas encadenadas pues la información solo se va a
    # consultar pero no a alterar por otro lado siempre se añade
    # un album, artista o canción
    # al final de la lista
    # cosa que no tiene repercusiones de tiempo en un arreglo
    catalog["albums"] = lt.newList('ARRAY_LIST', cmpfunction=compareAlbums)
    catalog["artists"] = lt.newList('ARRAY_LIST', cmpfunction=compareArtists)
    catalog["tracks"] = lt.newList('ARRAY_LIST', cmpfunction=compareTracks)

    return catalog


# Funciones para agregar informacion al catalogo
def addAlbum(catalog, albumdic):
    neoAlbum = newAlbum(albumdic)
    lt.addLast(catalog['albums'], neoAlbum)
    return catalog


def addArtist(catalog, artistdic):
    lt.addLast(catalog["artists"], artistdic)
    return catalog


def addTrack(catalog, track):
    lt.addLast(catalog['tracks'], track)
    return catalog
# Funciones para creacion de datos


def newAlbum(albumdic):
    if albumdic["release_date"].startswith(("Jan", "Feb", "Mar", "Apr",
                                            "May", "Jun", "Jul", "Aug",
                                            "Sep", "Oct", "Nov", "Dec")):

        date_format = dt.strptime(albumdic["release_date"], "%b-%y")
        anio = int(dt.strftime(date_format, "%Y"))

        if anio > 2022:
            anio = anio - 1000

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
    return lt.size(catalog['artists'])


def trackSize(catalog):
    return lt.size(catalog['tracks'])


# Funciones utilizadas para comparar elementos dentro de una lista
def compareAlbums(album1, album2):
    return album1["release_date"] < album2["release_date"]


def compareArtists(artist1, artist2):
    if float(artist1["artist_popularity"]) > float(artist2["artist_popularity"]):
        return float(artist1["artist_popularity"]) > float(artist2["artist_popularity"])
    else:
        pass

    if float(artist1["artist_popularity"]) == float(artist2["artist_popularity"]):
        return float(artist1["followers"]) > float(artist2["followers"])
    else:
        pass

    if float(artist1["followers"]) == float(artist2["followers"]):
        return artist1["name"] > artist2["name"]
    else:
        pass


def compareTracks(track1, track2):
    try:
        if float(track1["popularity"]) > float(track2["popularity"]):
            return float(track1["popularity"]) > float(track2["popularity"])
        else:
            pass

    except ValueError:
        if track1["popularity"].strip() == '':
            track1["popularity"] = 0

        if track2["popularity"].strip() == '':
            track2["popularity"] = 0

        if float(track1["popularity"]) > float(track2["popularity"]):
            return float(track1["popularity"]) > float(track2["popularity"])

    try:

        if float(track1["popularity"]) == float(track2["popularity"]):
            return float(track1["duration_ms"]) > float(track2["duration_ms"])
        else:
            pass

    except ValueError:
        if track1["duration_ms"] == '':
            track1["duration_ms"] = 0
        
        if track2["duration_ms"] == '':
            track2["duration_ms"] = 0
        
        if float(track1["popularity"]) == float(track2["popularity"]):
            return float(track1["duration_ms"]) > float(track2["duration_ms"])
    try:

        if float(track1["duration_ms"]) == float(track2["duration_ms"]):
            return track1["name"] > track2["name"]
        else:
            pass
    except ValueError:
        if track1["duration_ms"] == '':
            track1["duration_ms"] = 0

        if track2["duration_ms"] == '':
            track2 ["duration_ms"] = 0
        
        if float(track1["duration_ms"]) == float(track2["duration_ms"]):
            return track1["name"] > track2["name"]
    
# Funciones de ordenamiento


def sortAlbums(catalog):
    sa.sort(catalog['albums'], compareAlbums)


def sortArtists(catalog):
    sa.sort(catalog['artists'], compareArtists)


def sortTracks(catalog):
    sa.sort(catalog['tracks'], compareTracks)
