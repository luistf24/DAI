#./app/app.py

from flask      import Flask, render_template
from markupsafe import escape

from ejercicios0.criba      import criba
from ejercicios0.sf         import suf
from ejercicios0.cor        import corchetes
from ejercicios0.cor        import es_correcto
from ejercicios0.ejercicio4 import apellido_n
from ejercicios0.ejercicio4 import correo
from ejercicios0.ejercicio4 import tarjeta_credito

import os

app = Flask(__name__, template_folder='static')

@app.route('/Hello')
def hello_world():
  return 'Hello, World!'


@app.route('/ejercicio1/<int:numero>')
def ejercicio1(numero):
    return str(criba(numero))


@app.route('/ejercicio2')
def ejercicio2():
    suf()
    return 'La salida está en el archivo ./archivos/salida.txt'


@app.route('/ejercicio3')
def ejercicio3():
    return str(es_correcto(corchetes(100)))


@app.route('/ejercicio4/apellido_n/<string:apellido>')
def ejercicio4_1(apellido):
    return apellido_n(apellido)


@app.route('/ejercicio4/correo/<string:correo_e>')
def ejercicio4_2(correo_e):
    return correo(correo_e)


@app.route('/ejercicio4/tarjeta/<string:tarjeta>')
def ejercicio4_3(tarjeta):
    return tarjeta_credito(tarjeta)


@app.route('/imagenes')
def imagen():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
