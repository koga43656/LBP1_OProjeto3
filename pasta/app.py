from flask import Flask
from controlers.controler import coisa_controlador
app= Flask(__name__)

app.register_blueprint(coisa_controlador)


if __name__ == '__main__':
    app.run(debug=True)