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
import pycountry
...
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros
def newController():
    """
    Crea una instancia del modelo
    """
    control = {'model': None}
    control['model'] = model.newCatalog()
    return control


# Funciones para la carga de datos
def loadData(control):

    catalog = control['model']
    albums = loadAlbums(catalog)
    artists = loadArtist(catalog)
    tracks = loadTracks(catalog)
    sortAlbums(catalog)
    sortArtists(catalog)
    sortTracks(catalog)

    return albums, artists, tracks


def loadAlbums(catalog):
    albumsfile = cf.data_dir + 'spotify-albums-utf8-small.csv'
    input_file_al = csv.DictReader(open(albumsfile, encoding='utf-8'))
    for album in input_file_al:
        model.addAlbum(catalog, album)
    return model.albumSize(catalog)


def loadArtist(catalog):
    artistsfile = cf.data_dir + 'spotify-artists-utf8-small.csv'
    input_file_ar = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file_ar:
        model.addArtist(catalog, artist)
    return model.artistSize(catalog)


def loadTracks(catalog):
    tracksfile = cf.data_dir + 'spotify-tracks-utf8-small.csv'
    input_file_tr = csv.DictReader(open(tracksfile, encoding='utf-8'))
    for track in input_file_tr:
        model.addTrack(catalog, track)
    return model.trackSize(catalog)


# Funciones de ordenamiento
def sortAlbums(catalog):
    model.sortAlbums(catalog)


def sortArtists(catalog):
    model.sortArtists(catalog)


def sortTracks(catalog):
    model.sortTracks(catalog)
# Funciones de consulta sobre el catálogo


def albumesPorAnio(control, anio_o, anio_f):

    albums = model.albumesPorAnio(control['model'], anio_o, anio_f)
    return albums


def getTopArtists(control, topN):
    return model.getTopArtists(control["model"], topN)


def getPopularTracks(control, nombre, pais):
    pa = pycountry.countries.search_fuzzy(str(pais))
    xa = pa[0].alpha_2
    return model.getPopularTracks(control["model"], nombre, xa), xa


def popularTracks(control, top):
    tracks = model.popularTracks(control['model'], top)
    return tracks


def discografiaArtista(control, nombreArtista):
    albums = model.discografiaArtista(control['model'], nombreArtista)
    return albums

def getTopCancionesAnio(control, topN, anioI, anioF):
    return model.getTopCancionesAnio(control["model"], topN, anioI, anioF)