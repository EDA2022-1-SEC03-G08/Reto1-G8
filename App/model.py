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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos.
El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newCatalog():

    catalog = {'albums': None,
               'artist': None,
               'tracks': None}

    catalog['albums'] = lt.newList('ARRAY_LIST')
    catalog['artist'] = lt.newList('SINGLE_LINKED')
    catalog['tracks'] = lt.newList('SINGLE_LINKED')
    return catalog


def newCatalog():
    """
    Inicializa el catálogo de tracks. Crea una lista vacia para guardar
    todos los tracks, adicionalmente, crea una lista vacia para los artistas,
    una lista vacia para los albumess. Retorna el catalogo inicializado.
    """
    catalog = {'albums': None,
               'artists': None,
               'tracks': None}

    catalog['albums'] = lt.newList('SINGLE_LINKED')
    catalog['artists'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareauthors)
    catalog['tracks'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparetagnames)
    return catalog


# Funciones para agregar informacion al catalogo
def addNewAlbum(catalog, album):
    neoAlbum = newAlbum(album)
    lt.addLast(catalog['albums'], neoAlbum)
    return catalog

<<<<<<< HEAD

def addNewArtist(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    return catalog
=======
def addAlbum(catalog, album):
    # Se adiciona el album a la lista de albumes
    lt.addLast(catalog['albums'], album)
    return catalog


def addArtist(catalog, artist):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(artist['relevante'], artist['relevante'])
    lt.addLast(catalog['artists'], t)
    return catalog


def addTrack(catalog, track):
    """
    Adiciona un tag a la lista de tags
    """
    t = newBookTag(track['relevante'], track['relevante'])
    lt.addLast(catalog['tracks'], t)
    return catalog

>>>>>>> 8227fa805e931465ecfd7af8193e06ba6594a623
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


# Funciones de consulta
def albumSize(catalog):
    return lt.size(catalog['albums'])


def artistSize(catalog):
    return lt.size(catalog['artist'])
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
