"""Crie as classes necessárias para um sistema de gerenciamento de uma biblioteca. Os
bibliotecários deverão preencher o sistema com o título do livro, os autores, o ano, a editora, a
edição e o volume. A biblioteca também terá um sistema de pesquisa (outro software), portanto
será necessário conseguir acessar os atributos típicos de pesquisa (nome, autor, …).

SOLUÇÃO: Sistema de bibliteca com função de cadastrar autor e livro. Pelo sistema se veriricar numero total de livros, empresta-se e devolve-se livros, analisa-se historico do momento e pesquisa informações gerais.
"""
class Biblioteca:
    def __init__(self, livros):
        self.livros = livros
        self.emprestados = []
        self.devolvidos = []

    def numeroTotal(self):
        total = len(self.livros)
        print(total)

    def emprestarLivro(self, livro):
        self.emprestados.append(livro)

    def devolverLivro(self, livro):
        if livro in self.emprestados:
            self.emprestados.remove(livro)
        self.devolvidos.append(livro)
    
    def historico(self):
        print(f"LIVROS EMPRESTADOS: {len(self.emprestados)}")
        for i in self.emprestados:
            print(f"{i.titulo}")

        print(f"LIVROS DEVOLVIDOS: {len(self.devolvidos)}")
        for i in self.devolvidos:
            print(f"{i.titulo}")

    def pesquisa(self, livro):
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor.nome}")
        print(f"Ano: {livro.ano}")
        print(f"Editora: {livro.editora}")
        print(f"Edição: {livro.edicao}")
        print(f"Volume: {livro.volume}")

class Livro:
    def __init__(self, titulo, autor, ano, editora, edicao, volume):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume

class Autor:
    def __init__(self, nome):
        self.nome = nome

autor1 = Autor("José Carlos")
autor2 = Autor("Collen Hoover")
autor3 = Autor("Machado de Assis")

livro1 = Livro("Extraordinario", autor1 , 2012, "Apex", 20, 3)
livro2 = Livro("5 minutos", autor3 , 1930, "Go", 10, 6)

biblioteca_RJ = Biblioteca([livro1, livro2])
biblioteca_RJ.numeroTotal()
biblioteca_RJ.pesquisa(livro1)

biblioteca_RJ.emprestarLivro(livro1)
biblioteca_RJ.emprestarLivro(livro2)
biblioteca_RJ.devolverLivro(livro1)

biblioteca_RJ.historico()

