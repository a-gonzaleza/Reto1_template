"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
from ADT import list as lt
from DataStructures import listiterator as it


"""
Se define la estructura de un catálogo de libros.
El catálogo tendrá tres listas, una para libros, otra para autores 
y otra para géneros
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de peliculas. Retorna el catalogo inicializado.
    """
    catalog = {'movies':None, 'directors':None, 'actors': None}
    catalog['movies'] = lt.newList('ARRAY_LIST')
    catalog['directors'] = lt.newList('ARRAY_LIST')
    catalog['actors'] = lt.newList('ARRAY_LIST')
    return catalog


def newActor (name, movie_id):
    """
    Crea una nueva estructura para almacenar los actores de una pelicula 
    """
    pass

def addActor (catalog, actor):
    """
    Adiciona un actor a la lista de actores
    """
    pass

def newDirector (name, movie_id):
    """
    Esta estructura almancena los directores de una pelicula.
    """
    director = {'name':'', 'movie_id':''}
    director ['name'] = name
    director ['movie_id'] = movie_id
    return director


def addDirector (catalog, director):
    """
    Adiciona un director a la lista de directores
    """
    d = newDirector (director['director_name'], director['id'])
    lt.addLast (catalog['directors'], d)



# Funciones de consulta

def getMoviesByDirector (catalog, dir_name):
    """
    Retorna las peliculas a partir del nombre del director
    """
    directorMoviesID=[]
    totalRating=0
    iterator = it.newIterator(catalog["directors"])
    while it.hasNext(iterator):
        element = it.next(iterator)
        if dir_name.lower() in element["name"].lower(): #filtrar por palabra clave 
             directorMoviesID.append(element["movie_id"])
    iterator = it.newIterator(catalog["movies"])
    while it.hasNext(iterator):
        element=it.next(iterator)
        if element["id"] in directorMoviesID:
            totalRating+=float(element["vote_average"])

    if len(directorMoviesID)>0:
        return print("Ha dirigido",len(directorMoviesID),"películas y su promedio es de",round(totalRating/len(directorMoviesID),3))
    else:
        return "No tiene películas"
def getGoodMoviesByDirector(catalog,dir_name):
    directorMoviesID=[]
    goodMovies=0
    iterator = it.newIterator(catalog["directors"])
    while it.hasNext(iterator):
        element = it.next(iterator)
        if dir_name.lower() in element["name"].lower(): #filtrar por palabra clave 
             directorMoviesID.append(element["movie_id"])
    iterator = it.newIterator(catalog["movies"])
    while it.hasNext(iterator):
        element=it.next(iterator)
        if element["id"] in directorMoviesID and float(element["vote_average"])>=6:
            goodMovies+=1
    if goodMovies>0:
        return print("Ha dirigido",goodMovies,"películas con valoraciones superiores a 6")
    else:
        return print("No ha dirigido películas con valoraciones mayores a 6")


