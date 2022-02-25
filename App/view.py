﻿import config as cf
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


def printInfo(control):
    """
    Esta función se encarga de imprimir la información de los primeros
    y ultimos tres elementos de cada categoria (album, artista, canción).

    Esto funciona establemente cuando las tres listas son de tipo ARRAY.
    """

    print("Primeros tres albumes \n")
    for i in range(1, 4):
        print(lt.getElement(control['model']['albums'], i))
        print('\n')

    print("Ultimos tres albumes \n")
    for i in range(-2, 1):
        print(lt.getElement(control['model']['albums'], i))
        print('\n')

    print("Primeros tres artistas \n")
    for i in range(1, 4):
        print(lt.getElement(control['model']['artists'], i))
        print('\n')

    print("Ultimos tres artistas \n")
    for i in range(-2, 1):
        print(lt.getElement(control['model']['artists'], i))
        print('\n')

    print("Primeras tres canciones \n")
    for i in range(1, 4):
        print(lt.getElement(control['model']['tracks'], i))
        print('\n')

    print("Ultimas tres canciones \n")
    for i in range(-2, 1):
        print(lt.getElement(control['model']['tracks'], i))
        print('\n')


control = newController()


def printAlbumsPorAnio(albums, anio_o, anio_f):
    size = lt.size(albums)
    if size:
        print(f"Estos son los albumes entre {anio_o} y {anio_f}: \n")
        print(f"Total de albums encontrados: {size} \n")
        print("Primeros tres elementos:\n")
        for i in range(1, 4):
            album = lt.getElement(albums, i)
            artist_dic = album['artist_dic']
            artist = []
            for artistName in lt.iterator(artist_dic):
                artist.append(artistName['name'])
            print(("Nombre: " + album['name'] +
                   ", Fecha publicación: " + str(album['release_date']) +
                   ", Tipo: " + album['album_type'] +
                   ", Artista: " + str(artist) + album['artist_id'] +
                   ", Total de canciones: " + album['total_tracks']))
        print("\n")
        print("Ultimos tres alementos:\n")
        for i in range(-2, 1):
            album = lt.getElement(albums, i)
            artist_dic = album['artist_dic']
            artist = []
            for artistName in lt.iterator(artist_dic):
                artist.append(artistName['name'])
            print(("Nombre: " + album['name'] +
                   ", Fecha publicación: " + str(album['release_date']) +
                   ", Tipo: " + album['album_type'] +
                   ", Artista: " + str(artist) + album['artist_id'] +
                   ", Total de canciones: " + album['total_tracks']))

    else:
        print("No hay albumes en estos periodos")


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
        printInfo(control)
        print(f"Cantidad de albumes cargados: {albums} \n")
        print(f"Cantidad de artistas cargados: {artists} \n")
        print(f"Cantidad de canciones cargadas: {tracks} \n")

    elif int(inputs[0]) == 2:
        anio_o = int(input("Ingrese año inicial de busqueda:\n"))
        anio_f = int(input("Ingrese año final de busqueda:\n"))
        albums = controller.albumesPorAnio(control, anio_o, anio_f)
        printAlbumsPorAnio(albums, anio_o, anio_f)

    elif int(inputs[0]) == 3:
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        continue
sys.exit(0)