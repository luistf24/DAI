from bson.json_util import dumps
from bson import BSON, ObjectId
from pymongo import MongoClient

from flask import Flask, Response, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

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


# para devolver una lista (GET), o añadir (POST)
@app.route('/api/recipes', methods=['GET', 'POST'])
def api_1_1():

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
            ret = db.recipes.insert_one(json)

            query = {"_id": ret.inserted_id()}

            return dumps(query)

        else:
            return jsonify({'error':'Content-Type not supported!'}), 500


# para devolver una, modificar o borrar
@app.route('/api/recipes/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_1_2(id):

    if request.method == 'GET':
        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)
    
        buscado = db.recipes.find_one(query)

        if buscado:
            return dumps(buscado)

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
                    db.recipes.update_one(query, {"$set": {"name": nombre}})

                if(request.form.get('ingredients')):
                    ingredientes = request.form['ingredients']
                    ingrediente = db.recipes.find({ query}, {'ingredients.name': {'$regex': ingredientes}}) 

                    if(ingrediente.count() == 0):
                        db.recipies.update_one(query, {"$push": {"ingredients": ingredientes}})

                    else:
                        db.recipes.update_one(query, {ingrediente: ingredientes})

            return dumps(query)

        else:
            return jsonify({'error':'Not found'}), 404

    elif request.method == 'DELETE':
        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)

        buscado = db.recipes.find_one(query)

        if buscado:
            db.recipes.delete_one(buscado)
            return dumps(query)

        else:
            return jsonify({'error':'Not found'}), 404

    else:
        return jsonify({'error':'Opción no valida'}), 400


class Api_2_1(Resource):

    def get(self):

        lista = []
        
        buscados = db.recipes.find().sort('name')
        for recipe in buscados:
            recipe['_id'] = str(recipe['_id']) # paso a string
            lista.append(recipe)

        return jsonify(lista)


    def post(self):

        content_type = request.headers.get('Content-Type')
        
        if (content_type == 'application/json'):
            json = request.get_json(force=True)
            ret = db.recipes.insert_one(json)

            query = {"_id": ret.inserted_id()}

            return dumps(query)

        else:
            return jsonify({'error':'Content-Type not supported!'}), 500


class Api_2_2(Resource):

    def get(self, id):

        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)
    
        buscado = db.recipes.find_one(query)

        if buscado:
            return dumps(buscado)

        else:
            return jsonify({'error':'Not found'}), 404


    def put(self, id):

        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)
        
        buscado = db.recipes.find_one(query)

        if buscado:
            if(request.form):
                if(request.form.get('name')):
                    nombre = request.form['name']
                    db.recipes.update_one(query, {"$set": {"name": nombre}})

                if(request.form.get('ingredients')):
                    ingredientes = request.form['ingredients']
                    ingrediente = db.recipes.find({ query}, {'ingredients.name': {'$regex': ingredientes}}) 

                    if(ingrediente.count() == 0):
                        db.recipies.update_one(query, {"$push": {"ingredients": ingredientes}})

                    else:
                        db.recipes.update_one(query, {ingrediente: ingredientes})

            return dumps(query)

        else:
            return jsonify({'error':'Not found'}), 404


    def delete(self, id):

        try:
            query = {"_id": ObjectId(id) }

        except:
            return jsonify(error_id)

        buscado = db.recipes.find_one(query)

        if buscado:
            db.recipes.delete_one(buscado)
            return dumps(query)

        else:
            return jsonify({'error':'Not found'}), 404


api.add_resource(Api_2_1, '/api2/recipes/')
api.add_resource(Api_2_2, '/api2/recipes/<id>')


