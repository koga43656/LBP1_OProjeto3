from flask import session

CAMPOS_LOGIN = ['nome', 'tipo']

def existe(campo):
    return campo in session

def get(campo):
    return session.get(campo)

def atualizar_login(campo, valor):
    session[campo] = valor

def limpar_login():
    for campo in CAMPOS_LOGIN:
        session.pop(campo, None)
