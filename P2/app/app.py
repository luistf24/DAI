from bson.json_util import dumps
from pymongo import MongoClient

from flask import Flask, Response

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')


@app.route('/recetas_de/<string:receta>')
def recetas_de(receta):

    recetas = db.recipes.find({ 'name': receta}) 

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    resJson = dumps(response)

    return Response(resJson, mimetype='application/json')


@app.route('/recetas_con/<string:receta>')
def recetas_con(receta):

    recetas = db.recipes.find({ 'ingredients.name': {'$regex': receta, '$options': 'i'}}) 

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    resJson = dumps(response)

    return Response(resJson, mimetype='application/json')


@app.route('/recetas_compuestas_de/<int:receta>/ingredientes')
def recetas_compuestas_de(receta):

    recetas = db.recipes.find({ 'ingredients': {'$size': receta}}) 

    lista_recetas = []
    for  receta in recetas:
        app.logger.debug(receta)  
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    resJson = dumps(response)

    return Response(resJson, mimetype='application/json')

