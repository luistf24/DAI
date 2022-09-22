#./app/app.py

from ejemplos.criba import criba
from ejemplos.sf import suf
from ejemplos.cor import corchetes

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
          
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


