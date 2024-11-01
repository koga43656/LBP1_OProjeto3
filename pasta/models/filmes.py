class Filme:
    def __init__(self, id, titulo, preco, genero):
        self.id = id
        self.titulo = titulo
        self.preco = preco
        self.genero = genero

FILMES = [
    Filme(1, "Inception", 15.00, "Sci-Fi"),
    Filme(2, "The Godfather", 10.00, "Drama"),
    Filme(3, "The Dark Knight", 12.00, "Action"),
    Filme(4, "Pulp Fiction", 8.00, "Crime"),
    Filme(5, "Forrest Gump", 10.00, "Drama")
]

class Usuario:
    def __init__(self, id, nome, senha, tipo='user'):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.tipo = tipo
USUARIOS = [
    Usuario(1, "admin", "admin123", "admin"),
    Usuario(2, "igorlindo", "odnilrogi"),
    Usuario(3, "koga", "sddsmaryclare"),
]
