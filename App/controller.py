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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {'model': None}
    control['model'] = model.newCatalog()
    return control


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
    catalog = control['model']
    albums = loadAlbums(catalog)
    artists = loadArtists(catalog)
    tracks = loadTracks(catalog)
    return albums, artists, tracks


def loadAlbums(catalog):
    albumsfile = cf.data_dir + 'Spotify/spotify-albums-utf8-5pct.csv'
    input_file = csv.DictReader(open(albumsfile, encoding='utf-8'))
    for album in input_file:
        model.addNewAlbum(catalog, album)
    return model.albumSize(catalog)


def loadArtists(catalog):
    artistfile = cf.data_dir + 'Spotify/spotify-artists-utf8-5pct.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addNewArtist(catalog, artist)
    return model.artistSize(catalog)

def loadTracks(catalog):
    trackfile = cf.data_dir + 'Spotify/spotify-tracks-utf8-5pct.csv'
    input_file = csv.DictReader(open(trackfile, encoding='utf-8'))
    for track in input_file:
        model.addNewTrack(catalog, track)
    return model.trackSize(catalog)


# Funciones de ordenamiento
def sortTracks(catalog):
    """
    Ordena los tracks por average_rating
    """
    model.sortTracks(catalog)

# Funciones de consulta sobre el catálogo
