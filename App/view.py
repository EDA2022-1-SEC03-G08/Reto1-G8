﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

    # control = {'model': catalog}
    # control = {'model': {'albums: []
    #                     'artist': []
    #                     'tracks': []
    #                    }
    #          }


control = newController()


def printMenu():
    print("""
Bienvenido
Por favor antes de continuar carga la información en el catálogo.

1- Cargar información en el catálogo
2- Listar los álbumes en un periodo de tiempo
3- Encontrar los artistas más populares
4- Clasificar las canciones por popularidad
5- Encontrar la canción más popular de un artista
6- Encontrar la discografia de un artista
7- Clasificar las canciones con mayor distribución
0- Salir
          """)


def loadData():
    """
    Función encargada de entregar la información de carga de los archivos.
    """
    albums, artists, tracks = controller.loadData(control)
    return albums, artists, tracks


def printAlbumsInfo(control):
    """
    Esta función se encarga de imprimir la información de los primeros
    y ultimos tres elementos de cada categoria (album, artista, canción).

    Esto funciona establemente cuando las tres listas son de tipo ARRAY.
    """
    print("===================="*7)
    print("Primeros tres albumes")
    print("===================="*7)
    for i in range(1, 4):

        album = lt.getElement(control['model']['albums'], i)
        name = album['name']
        release_date = album['release_date']
        artistas = []
        rev_tracks = []
        total_tracks = album['total_tracks']
        album_type = album['album_type']
        external_url = album['external_urls']

        for artist in lt.iterator(album['artist_dic']):
            artistas.append(artist['name'])
            for track in lt.iterator(artist['all_tracks']):
                if album['track_id'].lower() == track['id'].lower():
                    rev_tracks.append(track['name'])

        if len(artistas) == 0:
            artistas = "No hay info"
        if len(rev_tracks) == 0:
            rev_tracks = "No hay info"

        print(f"||Nombre: {name}\n  "
              f"||Fecha publicación: {release_date}\n  "
              f"||Artistas: {artistas}\n  "
              f"||Canción relevante: {rev_tracks}\n  "
              f"||Canciones totales: {total_tracks}\n  "
              f"||Tipo del album: {album_type}\n  "
              f"||Urls externos: {external_url}||")

        print('\n')
    print("===================="*7)
    print("Ultimos tres albumes")
    print("===================="*7)
    for i in range(-2, 1):
        album = lt.getElement(control['model']['albums'], i)
        name = album['name']
        release_date = album['release_date']
        artistas = []
        rev_tracks = []
        total_tracks = album['total_tracks']
        album_type = album['album_type']
        external_url = album['external_urls']

        for artist in lt.iterator(album['artist_dic']):
            artistas.append(artist['name'])
            for track in lt.iterator(artist['all_tracks']):
                if album['track_id'].lower() == track['id'].lower():
                    rev_tracks.append(track['name'])

        if len(artistas) == 0:
            artistas = "No hay info"
        if len(rev_tracks) == 0:
            rev_tracks = "No hay info"

        print(f"||Nombre: {name}\n  "
              f"||Fecha publicación: {release_date}\n  "
              f"||Artistas: {artistas}\n  "
              f"||Canción relevante: {rev_tracks}\n  "
              f"||Canciones totales: {total_tracks}\n  "
              f"||Tipo del album: {album_type}\n  "
              f"||Urls externos: {external_url}||  ")

        print('\n')


def printArtistInfo(control):
    print("===================="*7)
    print("Primeros tres artistas")
    print("===================="*7)
    for i in range(1, 4):

        artist = lt.getElement(control['model']['artists'], i)
        name = artist['name']
        popularity = artist['artist_popularity']
        followers = artist['followers']
        genres = artist['genres']
        rev_tracks = []
        for track in lt.iterator(artist['all_tracks']):
            if artist['track_id'].lower() == track['id'].lower():
                rev_tracks.append(track['name'])
        if len(genres) == 0:
            genres = "No hay generos asociados"
        if len(rev_tracks) == 0:
            rev_tracks = "No se encontro la canción relevante"

        print(f"||Nombre: {name}\n  "
              f"||Popularidad: {popularity}\n  "
              f"||Seguidores: {followers}\n  "
              f"||Canción relevante: {rev_tracks}\n  "
              f"||Generos: {genres}||")

        print('\n')
    print("===================="*7)
    print("Ultimos tres artistas")
    print("===================="*7)
    for i in range(-2, 1):

        artist = lt.getElement(control['model']['artists'], i)
        name = artist['name']
        popularity = artist['artist_popularity']
        followers = artist['followers']
        genres = artist['genres']
        rev_tracks = []
        for track in lt.iterator(artist['all_tracks']):
            if artist['track_id'].lower() == track['id'].lower():
                rev_tracks.append(track['name'])

        if len(genres) == 0:
            genres = "No hay generos asociados"
        elif genres[0] == []:
            genres = "No hay generos asociados"
        if len(rev_tracks) == 0:
            rev_tracks = "No se encontro la canción relevante"

        print(f"||Nombre: {name}\n  "
              f"||Popularidad: {popularity}\n  "
              f"||Seguidores: {followers}\n  "
              f"||Canción relevante: {rev_tracks}\n  "
              f"||Generos: {genres}||")

        print('\n')


def printTrackInfo(control):
    print("===================="*7)
    print("Primeras tres canciones")
    print("===================="*7)
    for i in range(1, 4):
        track = lt.getElement(control['model']['tracks'], i)
        name = track['name']
        popularity = track['popularity']
        disc_num = track['disc_number']
        track_num = track['track_number']
        duration = track['duration_ms']
        href = track['href']
        artistas = []
        album_name = " "
        for album in lt.iterator(control['model']['albums']):
            if track['album_id'].lower() == album['id'].lower():
                album_name = album['name']
        for artist in lt.iterator(control['model']['artists']):
            if artist['id'].lower() in track['artists_id'].lower():
                artistas.append(artist['name'])

        print(f"||Nombre: {name}\n  "
              f"||Popularidad: {popularity}\n  "
              f"||Nombre album: {(album_name)}\n  "
              f"||Disc Number: {disc_num}\n  "
              f"||Track number: {track_num}\n  "
              f"||Duración (MS): {duration}\n  "
              f"||Artistas: {(artistas)}\n  "
              f"||Href: {href}||  ")

        print('\n')

    print("===================="*7)
    print("Ultimas tres canciones")
    print("===================="*7)
    for i in range(-2, 1):
        track = lt.getElement(control['model']['tracks'], i)
        name = track['name']
        popularity = track['popularity']
        disc_num = track['disc_number']
        track_num = track['track_number']
        duration = track['duration_ms']
        href = track['href']
        artistas = []
        album_name = " "
        for album in lt.iterator(control['model']['albums']):
            if track['album_id'].lower() == album['id'].lower():
                album_name = album['name']
        for artist in lt.iterator(control['model']['artists']):
            if artist['id'].lower() in track['artists_id'].lower():
                artistas.append(artist['name'])

        print(f"||Nombre: {name}\n  "
              f"||Popularidad: {popularity}\n  "
              f"||Nombre album: {(album_name)}\n  "
              f"||Disc Number: {disc_num}\n  "
              f"||Track number: {track_num}\n  "
              f"||Duración (MS): {duration}\n  "
              f"||Artistas: {artistas}\n  "
              f"||Href: {href}||")
        print('\n')


def printAlbumsPorAnio(albums, anio_o, anio_f):
    size = lt.size(albums)
    if size:
        print("===================="*7)
        print(f"Estos son los albumes entre {anio_o} y {anio_f}: \n")
        print(f"Total de albums encontrados: {size}")
        print("===================="*7)
        print("\n")
        print("===================="*7)
        print("Primeros tres elementos:")
        print("===================="*7)

        for i in range(1, 4):
            album = lt.getElement(albums, i)
            artist_dic = album['artist_dic']
            artist = []
            for artistName in lt.iterator(artist_dic):
                artist.append(artistName['name'])

            print(f"||Nombre: {album['name']}\n  "
                  f"||Fecha publicación: {str(album['release_date'])}\n  "
                  f"||Tipo: {album['album_type']}\n  "
                  f"||Artistas: {artist}\n  "
                  f"||Total de canciones: {album['total_tracks']}\n  "
                  f"||Urls externos: {album['external_urls']}\n  ")

        print("===================="*7)
        print("Ultimos tres alementos:")
        print("===================="*7)
        for i in range(-2, 1):
            album = lt.getElement(albums, i)
            artist_dic = album['artist_dic']
            artist = []
            for artistName in lt.iterator(artist_dic):
                artist.append(artistName['name'])

            print(f"||Nombre: {album['name']}\n  "
                  f"||Fecha publicación: {str(album['release_date'])}\n  "
                  f"||Tipo: {album['album_type']}\n  "
                  f"||Artistas: {artist}\n  "
                  f"||Total de canciones: {album['total_tracks']}\n  "
                  f"||Urls externos: {album['external_urls']}\n  ")
    else:
        print("No hay albumes en estos periodos")


def printPopularTracks(tracks, top, albums):
    size = lt.size(tracks)
    if size:
        if top > size:
            top = size
        print("===================="*7)
        print(f"Este es el top {top} de canciones: \n")
        print(f"Total de canciones: {size}")
        print("===================="*7)
        print("\n")
        print("===================="*7)
        print("Primeros tres elementos:")
        print("===================="*7)
        for i in range(1, 4):

            track = lt.getElement(tracks, i)
            album_name = " "
            lista_artistas = []
            lyrics = track['lyrics']
            if lyrics == "-99":
                lyrics = "Letra no disponible"

            for album in lt.iterator(albums):
                if track['album_id'].lower() == album['id'].lower():
                    album_name = album['name']
            for artist in lt.iterator(control['model']['artists']):
                if artist['id'].lower() in track['artists_id'].lower():
                    lista_artistas.append(artist['name'])

            print(f"||Popularidad: {track['popularity']}\n  "
                  f"||Duración: {track['duration_ms']}\n  "
                  f"||Nombre: {track['name']}\n  "
                  f"||Disc number: {track['disc_number']}\n  "
                  f"||Track number: {track['track_number']}\n  "
                  f"||Nombre album: {album_name}\n  "
                  f"||Artistas: {lista_artistas}\n  "
                  f"||Href: {track['href']}\n  "
                  f"||Lyrics: {lyrics}\n  ")
        print("===================="*7)
        print("Ultimos tres elementos:")
        print("===================="*7)
        for i in range(-2, 1):

            track = lt.getElement(tracks, i)
            album_name = " "
            lista_artistas = []
            lyrics = track['lyrics']
            if lyrics == "-99":
                lyrics = "Letra no disponible"

            for album in lt.iterator(albums):
                if track['album_id'].lower() == album['id'].lower():
                    album_name = album['name']
            for artist in lt.iterator(control['model']['artists']):
                if artist['id'].lower() in track['artists_id'].lower():
                    lista_artistas.append(artist['name'])

            print(f"||Popularidad: {track['popularity']}\n  "
                  f"||Duración: {track['duration_ms']}\n  "
                  f"||Nombre: {track['name']}\n  "
                  f"||Disc number: {track['disc_number']}\n  "
                  f"||Track number: {track['track_number']}\n  "
                  f"||Nombre album: {album_name}\n  "
                  f"||Artistas: {lista_artistas}\n  "
                  f"||Href: {track['href']}\n  "
                  f"||Lyrics: {lyrics}\n  ")


def printDiscografiaArtista(albums, nombreArtista):
    size = lt.size(albums)
    tipoSingle = 0
    tipoAlbum = 0
    tipoCompilation = 0
    if size:
        for album in lt.iterator(albums):
            if album['album_type'] == "album":
                tipoAlbum += 1
            elif album['album_type'] == "compilation":
                tipoCompilation += 1
            elif album['album_type'] == "single":
                tipoSingle += 1

        print("===================="*7)
        print(f"Tamaño de la discografia de {nombreArtista}: {size}")
        print(f"Compilation {tipoCompilation}")
        print(f"single: {tipoSingle}")
        print(f"album: {tipoAlbum}")
        print("===================="*7)

        print("===================="*7)
        print("Detalle de los albums")
        print("===================="*7)
        print("\n")
        print("===================="*7)
        print("Primeros tres alementos:")
        print("===================="*7)
        if size < 3:
            longitud = size+1
        elif size >= 3:
            longitud = 4
        for i in range(1, longitud):
            album = lt.getElement(albums, i)
            artist_dic = album['artist_dic']
            artist = []
            tracks_list = []
            for artistName in lt.iterator(artist_dic):
                artist.append(artistName['name'])
            for cancion in lt.iterator(control['model']['tracks']):
                if cancion['album_id'] == album['id']:
                    tracks_list.append(cancion)
            print(tracks_list)

            print(f"||Nombre: {album['name']}\n  "
                  f"||Fecha publicación: {str(album['release_date'])}\n  "
                  f"||Tipo: {album['album_type']}\n  "
                  f"||Artistas: {artist}\n  "
                  f"||Total de canciones: {album['total_tracks']}\n  "
                  f"||Urls externos: {album['external_urls']}\n  ")


        print("===================="*7)
        print("Ultimos tres alementos:")
        print("===================="*7)
        if size >= 4:

            for i in range(-2, 1):
                album = lt.getElement(albums, i)
                artist_dic = album['artist_dic']
                artist = []
                tracks_list = []
                for artistName in lt.iterator(artist_dic):
                    artist.append(artistName['name'])
                for cancion in lt.iterator(control['model']['tracks']):
                    if cancion['album_id'] == album['id']:
                        tracks_list.append(cancion)
                print(tracks_list)

                print(f"||Nombre: {album['name']}\n  "
                      f"||Fecha publicación: {str(album['release_date'])}\n  "
                      f"||Tipo: {album['album_type']}\n  "
                      f"||Artistas: {artist}\n  "
                      f"||Total de canciones: {album['total_tracks']}\n  "
                      f"||Urls externos: {album['external_urls']}\n  ")

                """
                print(f"||Nombre: {name}\n  "
                      f"||Popularidad: {popularity}\n  "
                      f"||Nombre album: {(album_name)}\n  "
                      f"||Disc Number: {disc_num}\n  "
                      f"||Track number: {track_num}\n  "
                      f"||Duración (MS): {duration}\n  "
                      f"||Artistas: {(artistas)}\n  "
                      f"||Href: {href}||  ")
                """
        else:
            print("solo hay tres o menos albumes en la discografia")
    else:
        print(f"No se encontro discografia de {nombreArtista}")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        # estas tres variables son numero de tipo int

        albums, artists, tracks = loadData()

        # este apartado se encarga de informar al usuario cuantos
        # elementos fueron cargados e incluye la función de imprimir
        # la información de cada lista.

        print("Cargando información de los archivos .... \n")
        printAlbumsInfo(control)
        printArtistInfo(control)
        printTrackInfo(control)
        print("===================="*2)
        print(f"Cantidad de albumes cargados: {albums} \n")
        print(f"Cantidad de artistas cargados: {artists} \n")
        print(f"Cantidad de canciones cargadas: {tracks}")
        print("===================="*2)

    elif int(inputs[0]) == 2:
        anio_o = int(input("Ingrese año inicial de busqueda:\n"))
        anio_f = int(input("Ingrese año final de busqueda:\n"))
        albums = controller.albumesPorAnio(control, anio_o, anio_f)
        printAlbumsPorAnio(albums, anio_o, anio_f)

    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        albums = control['model']['albums']
        top = int(input("Esta buscando el top...\n"))
        tracks = controller.popularTracks(control, top)
        printPopularTracks(tracks, top, albums)

    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        nombre = input("Que artista desea buscar: \n")
        albums = controller.discografiaArtista(control, nombre)
        printDiscografiaArtista(albums, nombre)
        pass
    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        continue
sys.exit(0)
