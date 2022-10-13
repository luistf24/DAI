from bson.json_util import dumps
from bson import BSON
from pymongo import MongoClient

from flask import Flask, Response, request, jsonify
from bson import ObjectId

app = Flask(__name__)

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

# Variables

error_id = {
    'error': 'Id inválido'
}

insertado = {
    'ok': 'Bebida nueva añadida'
}

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


# para devolver una lista (GET), o añadir (POST)
@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1():

    if request.method == 'GET':
        lista = []
        buscados = db.recipes.find().sort('name')

        for recipe in buscados:
            recipe['_id'] = str(recipe['_id']) # paso a string
            lista.append(recipe)

        return jsonify(lista)

    elif request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        
        if (content_type == 'application/json'):
            json = request.get_json(force=True)
            db.recipes.insert_one(json)

            return añadido 

        else:
            print('Content-Type not supported!')

    else:
        return 'Algo falla'


# para devolver una, modificar o borrar
@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):

    if request.method == 'GET':
        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)
    
        buscado = db.recipes.find_one(query)

        if buscado:
            return buscado 

        else:
            return jsonify({'error':'Not found'}), 404

    elif request.method == 'PUT':
        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)
        
        buscado = db.recipes.find_one(query)

        if buscado:
            if(request.form):
                if(request.form.get('name')):
                    nombre = request.form['name']

                else:
                    nombre = buscado.get('name')

                if(request.form.get('ingredients')):
                    ingredientes = request.form['ingredients']

                else:
                    ingredientes = buscado.get('ingredients')
                
                db.recipes.update_one(query, {"$set": {"name": nombre, "ingredients": ingredientes}})

        else:
            return jsonify({'error':'Not found'}), 404

    elif request.method == 'DELETE':
        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)

        buscado = db.recipes.find_one(query)

        if buscado:
            recipes.delete_one(buscado)
            return buscado

        else:
            return jsonify({'error':'Not found'}), 404

    else:
        return jsonify({'error':'Opción no valida'}), 400
