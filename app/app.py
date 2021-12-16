"""A simple flask web app"""

from flask import Flask, render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():

    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():

    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/OOPC")
def OOPC_get():
    return render_template('OOPC.html')

@app.route("/SE")
def SE_get():
    return render_template('SE.html')

@app.route("/OOPV")
def OOPV_get():
    return render_template('OOPV.html')

@app.route("/AAA")
def AAA_get():
    return render_template('AAA.html')

