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
from DISClib.Algorithms.Sorting import mergesort as sa
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
               "artists": None,
               "tracks": None}
    # No se neceistan listas encadenadas pues la información solo se va a
    # consultar pero no a alterar. Por otro lado siempre se añade
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
    neoArtist = newArtist(artistdic)
    for album in lt.iterator(catalog["albums"]):
        artists = (album["artist_id"].strip()).lower()
        if neoArtist['id'].lower() in artists:
            if lt.isPresent(album['artist_dic'], neoArtist) == 0:
                lt.addLast(album['artist_dic'], neoArtist)
    lt.addLast(catalog["artists"], neoArtist)
    return catalog


def addTrack(catalog, track):
    for artist in lt.iterator(catalog['artists']):
        tracks = (track['artists_id'].strip()).lower()
        if artist['id'].lower() in tracks:
            lt.addLast(artist["all_tracks"], track)
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
            anio = anio - 100

    else:
        try:
            date_format = dt.strptime(albumdic["release_date"], "%Y-%m-%d")
            anio = int(dt.strftime(date_format, "%Y"))

        except ValueError:
            date_format = dt.strptime(albumdic["release_date"], "%Y")
            anio = int(dt.strftime(date_format, "%Y"))

    albumdic["release_date"] = anio
    albumdic['artist_dic'] = lt.newList('ARRAY_LIST')

    return albumdic


def newArtist(artistdic):
    artistdic["all_tracks"] = lt.newList("ARRAY_LIST", cmpfunction=compareTracks)

    return artistdic
# Funciones de consulta


def albumesPorAnio(catalog, anio_o, anio_f):
    """
    retorna una lista de albumes en in periodo de tiempo
    """
    albums = catalog['albums']
    lista_albums = lt.newList("ARRAY_LIST")
    for album in lt.iterator(albums):
        if (album['release_date'] >= anio_o) and (album['release_date'] <= anio_f):
            lt.addLast(lista_albums, album)
    return lista_albums


def getTopArtists(list, topN):
    artistas = list["artists"]
    lista_artistas = lt.newList("ARRAY_LIST")
    for pos in range(topN):
        lt.addLast(lista_artistas, lt.getElement(artistas, pos+1))
    return lista_artistas


def getPopularTracks(list, nombre, pais):
    albumes = list["albums"]
    albumsAndThings = lt.newList("ARRAY_LIST")
    validAlbums = lt.newList("ARRAY_LIST")
    validArtist = lt.newList("ARRAY_LIST")
    validTracks = lt.newList("ARRAY_LIST")
    for album in lt.iterator(albumes):
# NO ES o(n)>2, ya que solo realiza el segundo loop en el caso de
# encontrar el artista buscado, y la segunda iteracion es o(1)
        if pais in album["available_markets"]:
            for artist in lt.iterator(album['artist_dic']):
                if (artist["name"] in nombre):
                    lt.addLast(validAlbums, album)
                    if lt.size(validArtist) == 0:
                        lt.addLast(validArtist, artist)
                        for track in lt.iterator(artist["all_tracks"]):
                            if pais in track["available_markets"]:
                                lt.addLast(validTracks, track)

    lt.addLast(albumsAndThings, validArtist)
    lt.addLast(albumsAndThings, validAlbums)
    lt.addLast(albumsAndThings, validTracks)
    return albumsAndThings
    
#TODO:REVISAR; FUNCION DE BONO

def getTopCancionesAnio(list, topN, anio_i, anio_f):
    validAlbums = albumesPorAnio(list, anio_i, anio_f)
    validTracks = lt.newList('ARRAY_LIST')
    finalTracks = lt.newList('ARRAY_LIST')
    for album in lt.iterator(validAlbums):
        for artist in lt.iterator(album["artist_dic"]):
            for track in lt.iterator(artist["all_tracks"]):
                lt.addLast(validTracks, track)
    sa.sort(validTracks, compareTracks)
    for song in range(topN):
        lt.addLast(finalTracks, lt.getElement(validTracks, song+1))

    return finalTracks, validAlbums
    

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
            track2["duration_ms"] = 0

        if float(track1["duration_ms"]) == float(track2["duration_ms"]):
            return track1["name"] > track2["name"]

# Funciones de ordenamiento


def sortAlbums(catalog):
    sa.sort(catalog['albums'], compareAlbums)


def sortArtists(catalog):
    sa.sort(catalog['artists'], compareArtists)


def sortTracks(catalog):
    sa.sort(catalog['tracks'], compareTracks)
