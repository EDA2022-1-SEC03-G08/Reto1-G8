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
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from datetime import datetime as dt

"""
Se define la estructura de un catálogo de videos.
El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newCatalog():

    catalog = {'albums': "",
               'artist': "",
               'tracks': ""}

    catalog['albums'] = lt.newList('ARRAY_LIST')
    catalog['artist'] = lt.newList('ARRAY_LIST')
    catalog['tracks'] = lt.newList('ARRAY_LIST')
    return catalog


# Funciones para agregar informacion al catalogo
def addNewAlbum(catalog, album):
    neoAlbum = newAlbum(album)
    lt.addLast(catalog['albums'], neoAlbum)
    return catalog


def addNewArtist(catalog, artist):
    neoArtist = newArtist(artist)
    lt.addLast(catalog['artist'], neoArtist)
    return catalog


def addNewTrack(catalog, track):
    neoTrack = newTrack(track)
    lt.addLast(catalog['tracks'], neoTrack)
    return catalog
# Funciones para creacion de datos


def newAlbum(album1):
    album = {'name': "", 'release_date': "", 'avalaible_markets': "",
             'total_tracks': "", 'type': "", 'artists': "",
             'external_urls': "", 'images': ""}

    album['name'] = album1['name']
    release_date = dt.strptime(album1['release_date'], "%Y-%m-%d")
    album['release_date'] = release_date
    album['available_markets'] = album1['available_markets']
    album['total_tracks'] = album1['total_tracks']
    album['type'] = album1['album_type']
    album['artists'] = lt.newList('ARRAY_LIST')
    album['external_urls'] = album1['external_urls']
    album['images'] = album1['images']
    return album


def newArtist(artist1):
    artist = {'name': "", 'popularity': "", 'genres': "",
              'followers': "", 'tracks': ""}
    artist['name'] = artist1['name']
    artist['popularity'] = artist1['artist_popularity']
    artist['genres'] = lt.newList('ARRAY_LIST')
    artist['followers'] = artist1['followers']
    artist['tracks'] = lt.newList('ARRAY_LIST')
    return artist


def newTrack(track1):
    track = {'name': "", 'album': "", 'artist': "",
             'popularity': "", 'available_markets': "", 'track_number': "",
             'duration_ms': "", 'preview_url': "", 'lyrics': ""}

    track['name'] = track1['name']
    track['album'] = lt.newList("ARRAYLIST")
    track['artist'] = lt.newList("ARRAY_LIST")
    track['popularity'] = track1['popularity']
    track['available_markets'] = track1['available_markets']
    track['track_number'] = track1['track_number']
    track['duration_ms'] = track1['duration_ms']
    track['preview_url'] = track1['preview_url']
    track['lyrics'] = track1['lyrics']
    return track


# Funciones de consulta
def anioAlbum(catalog):
    return catalog['albums']


def albumSize(catalog):
    return lt.size(catalog['albums'])


def artistSize(catalog):
    return lt.size(catalog['artist'])


def trackSize(catalog):
    return lt.size(catalog['tracks'])
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
