#./app/app.py

from flask import Flask, render_template
from markupsafe import escape

from ejercicios0.criba import criba
from ejercicios0.sf import suf
from ejercicios0.cor import corchetes

import os

app = Flask(__name__, template_folder='static')

@app.route('/Hello')
def hello_world():
  return 'Hello, World!'


@app.route('/prueba/ejercicio1/<int:numero>')
def ejercicio1(numero):
    return str(criba(numero))

@app.route('/prueba/ejercicio2')
def ejercicio2():
    suf()
    return 'La salida está en el archivo ./archivos/salida.txt'

@app.route('/prueba/ejercicio3')
def ejercicio3():
    return corchetes()

@app.route('/prueba/imagenes')
def imagen():
    return render_template('index.html')
