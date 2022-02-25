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
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
#TODO: De lab 4 borrar!!!
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import mergesort as mes
from DISClib.Algorithms.Sorting import quicksort as qus
#
from datetime import datetime as dt
assert cf

"""
Se define la estructura de un catálogo de Spotify.
El catálogo tendrá tres listas, una para los albumes, otra para las artistas
y otra para las canciones.
"""


# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de tracks. Crea una lista vacia para guardar
    todos los tracks, adicionalmente, crea una lista vacia para los artistas,
    una lista vacia para los albumess. Retorna el catalogo inicializado.
    """

    catalog = {'albums': None,
               'artists': None,
               'tracks': None}

    catalog['albums'] = lt.newList('ARRAY_LIST')
    catalog['artists'] = lt.newList('ARRAY_LIST')
    catalog['tracks'] = lt.newList('SINGLE_LINKED')
    return catalog


# Funciones para agregar informacion al catalogo
def addNewAlbum(catalog, album):
    neoAlbum = newAlbum(album)
    lt.addLast(catalog['albums'], neoAlbum)
    return catalog


def addNewArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    return catalog


def addNewTrack(catalog, track):
    lt.addLast(catalog['tracks'], track)
    return catalog

# Funciones para creacion de datos




def newAlbum(album1):
    album = {'name': "", 'release_date': "", 'avalaible_markets': None,
             'total_tracks': None, 'type': "", 'artists': None,
             'external_urls': "", 'images': ""}

    album['name'] = album1['name']
    album['release_date'] = album1['release_date']
    album['available_markets'] = album1['available_markets']
    album['total_tracks'] = album1['total_tracks']
    album['type'] = album1['album_type']
    album['artists'] = lt.newList('ARRAY_LIST')
    album['external_urls'] = album1['external_urls']
    album['images'] = album1['images']
    return album


def newArtist(artist1):
    artist = {'name': "", 'popularity': "", 'genres': "",
              'followers': "", 'tracks': None}
    artist['name'] = artist1['name']
    artist['popularity'] = artist1['popularity']
    artist['genres'] = lt.newList('ARRAY_LIST')
    return artist

def newTrack(track1):
    track = {'name': "", 'popularity': "", 'genres': "",
              'album_id': "", 'artist_id': None}
    track['name'] = track1['name']
    track['popularity'] = track1['popularity']
    track['artist_id'] = lt.newList('ARRAY_LIST')
    track['album_id'] = track1['album_id']
    return track

# Funciones de consulta

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

#TODO: Borrar despues del lab 4:
def sortArtistslab(catalog, size, ttype, sorter):
    sub_list = lt.subList(catalog['artists'], 1, int((size/100)*artistSize(catalog)))
    start_time = time.time()
    sorted_list = lt.newList(ttype)
    if sorter.lower() in "shell":
        print("Sorting con shell...")
        sorted_list = sa.sort(sub_list, compareFollowers)
    elif sorter.lower() in "insertion":
        print("Sorting con insertion...")
        sorted_list = ins.sort(sub_list, compareFollowers)
    elif sorter.lower() in "selection":
        print("Sorting con selection...")
        sorted_list = ses.sort(sub_list, compareFollowers)
    elif sorter.lower() in "merge":
        print("Sorting con merge...")
        sorted_list = mes.sort(sub_list, compareFollowers)
    else:
        print("Sorting con quick...")
        sorted_list = qus.sort(sub_list, compareFollowers)
    end_time = time.time()
    delta_time = end_time - start_time
    return sorted_list, delta_time

def compareFollowers(artist1, artist2):
    return (float(artist1['followers']) < float(artist2['followers']))



def sortTracks(catalog):
    sa.sort(catalog['tracks'], compareTracks)