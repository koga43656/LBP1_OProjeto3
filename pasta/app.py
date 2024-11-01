from flask import Flask, render_template, request, redirect, url_for
from controllers import koga
from models import filmes, sessoes

app = Flask(__name__)
app.register_blueprint(koga)
app.secret_key = 'senha super secreta'

@app.errorhandler(404)
def page_not_found(error):
    return 'Página não encontrada', 404

@app.errorhandler(401)
def acesso_negado(error):
    return 'Acesso negado!', 401

@app.before_request
def b4_request():
    if request.path == 'koga.login':
        return
    if not sessoes.existe('nome'):
        return redirect(url_for('koga.login'))

@app.after_request
def a_request(response):
    print("Depois da requisição")
    return response

@app.route('/')
def index():
    carr = []
    for f in filmes.FILMES:
        cookie = request.cookies.get(f'filme_{f.id}')
        if cookie:
            carr.append({
                'titulo': f.titulo,
                'quantidade': int(cookie),
                'total': int(cookie) * f.preco
            })
    return render_template('index.html', nome=sessoes.get('nome'), filmes=filmes.FILMES, carrinho=carr)

if __name__ == '__main__':
    app.run(debug=True)
