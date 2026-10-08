from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    livros = session.scalars(select(Livro)).all()

    for livro in livros:
        status = "disponível" if livro.disponivel else "indisponível"
        print(f"{livro.titulo} - Autor: {livro.autor.nome} - {status}")

    return livros


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    livros = session.scalars(
        select(Livro).where(Livro.disponivel == True)
    ).all()

    for livro in livros:
        print(f"{livro.titulo} - Autor: {livro.autor.nome}")

    return livros


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    livros = session.scalars(
        select(Livro).where(Livro.titulo.contains(trecho))
    ).all()

    for livro in livros:
        print(f"{livro.titulo} - Autor: {livro.autor.nome}")

    return livros


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    autor = session.scalar(
        select(Autor).where(Autor.nome == nome_autor)
    )

    if autor is None:
        print("Autor não encontrado.")
        return []

    for livro in autor.livros:
        print(f"{livro.titulo} - {livro.ano}")

    return autor.livros
