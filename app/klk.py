from flask import Flask

app = Flask(__name__)

@app.route('/klk')
def klk():
    return 'klk main'

