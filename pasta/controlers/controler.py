from flask import Flask, Blueprint, render_template
from models.model import c

coisa_controlador = Blueprint("coisa",__name__)



@coisa_controlador.route("/")
def hello_world():
   
    return render_template('index.html', ok = c)
    