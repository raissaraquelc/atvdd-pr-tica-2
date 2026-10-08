# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

1. Para que serve o campo `disponivel` em `Livro`?

Ele informa se o livro está disponível para empréstimo ou se já está emprestado.

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?

Porque o `commit()` salva a alteração no banco de dados.

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?

Na função `listar_livros`, usando `livro.autor.nome`, e também em `listar_livros_por_autor`, usando `autor.livros`.
