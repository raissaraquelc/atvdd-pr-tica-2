from sqlalchemy import select

from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    if session.scalar(select(Autor)) is not None:
        return

    autor1 = Autor(nome="Machado de Assis", pais="Brasil")
    session.add(autor1)

    autores = [
        Autor(nome="Jorge Amado", pais="Brasil"),
        Autor(nome="Clarice Lispector", pais="Brasil"),
    ]
    session.add_all(autores)

    livros = [
        Livro(titulo="Dom Casmurro", ano=1899, autor=autor1, disponivel=True),
        Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=autor1, disponivel=False),
        Livro(titulo="O Cortiço", ano=1890, autor=autor1, disponivel=True),
        Livro(titulo="Gabriela, Cravo e Canela", ano=1958, autor=autores[0], disponivel=True),
        Livro(titulo="Dona Flor e Seus Dois Maridos", ano=1966, autor=autores[0], disponivel=False),
        Livro(titulo="A Hora da Estrela", ano=1977, autor=autores[1], disponivel=True),
    ]
    session.add_all(livros)
    session.commit()
