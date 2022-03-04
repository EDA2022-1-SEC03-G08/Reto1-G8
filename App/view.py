from re import I
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

def printTopArtistas(topArtistas):
    con = 0
    numN = topN
    print("===================="*7)
    print("Primeros tres artistas")
    print("===================="*7)
    while numN > 0 and con < 3:
        artistN = lt.getElement(topArtistas, con + 1)
        #Se busca la track mas popular en la lista de tracks del artista
        # Resulta O(1) ya que la lista iterada es notablemente menor que
        # n total de datos
        nombreCancion = ""
        for el in lt.iterator(artistN["all_tracks"]):
            if el["id"] == artistN["track_id"]:
                nombreCancion = el["name"]
                break
        printArtista(artistN["name"], artistN["artist_popularity"], artistN["followers"], artistN["genres"], nombreCancion)
        numN -= 1
        con += 1
    if numN < 3:
        con = numN
        numN = 3
    numN += 1
    print("===================="*7)
    print("Ultimos tres artistas")
    print("===================="*7)
    while con > 0:
        artistN = lt.getElement(topArtistas, numN)
        nombreCancion = ""
        for el in lt.iterator(artistN["all_tracks"]):
            if el["id"] == artistN["track_id"]:
                nombreCancion = el["name"]
                break
        printArtista(artistN["name"], artistN["artist_popularity"], artistN["followers"], artistN["genres"], nombreCancion)
        numN += 1
        con -= 1

def printArtista(name, popularity, followers, genres, topSong):
    print("\n")
    print("Nombre: " + name + "\n")
    print("Popularidad: " + popularity + "\n")
    print("Followers: " + followers + "\n")
    print("Generos: " + genres + "\n")
    print("Cancion referente: " + topSong + "\n")

def printCancion(name, nombreAlbum, fecha, artistas, duration, popularity ,url, letra):
    print("\n")
    print("Nombre: " + name + "\n")
    print("Album: " + nombreAlbum + "\n")
    print("Fecha de publicación: " + str(fecha) + "\n")
    print("Artistas: ")
    for a in artistas.split():
        print(a + " \n")
    print("Duración: " + str(duration) + "\n")
    print("Popularidad: " + popularity + "\n")
    print("URL preview: " + url + "\n")
    print("Letra: " + letra + "\n")

def printCancionespPorRegion(size, artists, albums, tracks):
    con = 0
    numN = size
    print("===================="*7)
    print("Primeras tres canciones")
    print("===================="*7)
    while numN > 0 and con < 3:
        cancion = lt.getElement(tracks, con + 1)
        nonmbreAlbum = "No identificado" 
        fechAlbum = "No identificada"
        nombreArtistas = ""
        for album in lt.iterator(albums):
            if cancion["album_id"] == album["id"]:
               nonmbreAlbum = album["name"] 
               fechAlbum = album["release_date"]
               for artist in lt.iterator(album["artist_dic"]):
                   nombreArtistas += artist["name"] + " "
               break
        letra = cancion["lyrics"]
        if letra == "-99":
            letra = "Letra de la canción NO disponible"
        letra = (letra[:150] + '\n...') if len(letra) > 150 else letra
        printCancion(cancion["name"], nonmbreAlbum, fechAlbum, nombreArtistas, cancion["duration_ms"], cancion["popularity"], cancion["preview_url"], letra)
        numN -= 1
        con += 1
    if numN < 3:
        con = numN
        numN = 3
    numN += 1
    print("===================="*7)
    print("Ultimas tres canciones")
    print("===================="*7)
    while con > 0:
        cancion = lt.getElement(tracks, con + 1)
        nonmbreAlbum = "No identificado" 
        fechAlbum = "No identificada"
        nombreArtistas = ""
        for album in lt.iterator(albums):
            if cancion["album_id"] == album["id"]:
               nonmbreAlbum = album["name"] 
               fechAlbum = album["release_date"]
               for artist in lt.iterator(album["artist_dic"]):
                   nombreArtistas += artist["name"] + " "
               break
        letra = cancion["lyrics"]
        if letra == "-99":
            letra = "Letra de la canción NO disponible"
        letra = (letra[:150] + '\n...') if len(letra) > 150 else letra
        printCancion(cancion["name"], nonmbreAlbum, fechAlbum, nombreArtistas, cancion["duration_ms"], cancion["popularity"], cancion["preview_url"], letra)
        numN += 1
        con -= 1

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

        topN = int(input("Ingrese el numero de artistas a encontrar:\n"))
        #Se busca cada elemento segun su posicion en la lista ya organizada y se
        #Imprime la info por cada artista
        topArtistas = controller.getTopArtists(control,topN)
        size = lt.size(topArtistas)
        if size:
            print("Los primeros y ultimos 3 artistas más populares en el top" + str(topN) + ":")
            printTopArtistas(topArtistas)
        else:
            print("0 artistas en TOP 0")

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        nobreArtist = input("Ingrese el nombre del artista:\n")
        nombrePais = input("Ingrese el nombre de país/mercado disponible de la canción:\n")

        artistaInfo, pais = controller.getPopularTracks(control, nobreArtist, nombrePais)
        size = lt.size(artistaInfo)
        if size:
            artist = lt.getElement(artistaInfo, 1)
            validAlbums = lt.getElement(artistaInfo, 2)
            validTracks = lt.getElement(artistaInfo, 3)
            x = lt.size(validAlbums)
            y = lt.size(validTracks)
            print("Discografia disponible de " + nobreArtist + " en " + nombrePais + " (" + pais + "): ")
            print("Albumes disponibles regionalmente: " + str(x))
            print("Canciones disponibles regionalmente: " + str(y) + "\n")
            print("Los primeras y ultimas 3 canciones más populares de " + nobreArtist + " en " + pais + ":")
            printCancionespPorRegion(y, artist, validAlbums, validTracks)
        else:
            print("No se encontro al artista.")

    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        continue
sys.exit(0)