﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.newCatalog()
    return control

# Funciones para la carga de datos

def loadData(control):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    albums = loadAlbums(catalog)
    artists = loadArtists(catalog)
    tracks = loadTracks(catalog)
    sortTracks(catalog)
    return albums, artists, tracks


def loadAlbums(catalog):
    """
    Carga los albumes del archivo.  Por cada album se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    albumsfile = cf.data_dir + 'Spotify/spotify-albums-utf8-5pct.csv'
    input_file = csv.DictReader(open(albumsfile, encoding='utf-8'))
    for album in input_file:
        model.addAlbum(catalog, album)
    return model.albumSize(catalog)


def loadArtists(catalog):
    """
    Carga todos los artistas del archivo y los agrega a la lista de artistas
    """
    artistsfile = cf.data_dir + 'Spotify/spotify-artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    return model.artistsSize(catalog)


def loadTracks(catalog):
    """
    Carga la información que asocia tags con tracks.
    """
    tracksfile = cf.data_dir + 'Spotify/spotify-tracks-utf8-5pct.csv'
    input_file = csv.DictReader(open(tracksfile, encoding='utf-8'))
    for track in input_file:
        model.addTrack(catalog, track)
    return model.tracksSize(catalog)


# Funciones de ordenamiento
def sortTracks(catalog):
    """
    Ordena los tracks por average_rating
    """
    model.sortTracks(catalog)

# Funciones de consulta sobre el catálogo
