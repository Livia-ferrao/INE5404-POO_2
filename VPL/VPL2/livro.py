from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def autores(self):
        return self.__autores

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    def incluirAutor(self, autor: Autor):
        if type(autor) is Autor:
            if autor not in self.__autores:
                self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        if type(autor) is Autor:
            if autor in self.__autores:
                self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        repetido = False
        for i in range(0,len(self.__capitulos)):
            if self.__capitulos[i].numero == numeroCapitulo:
                repetido =True
        if not repetido:
            capi = Capitulo(numeroCapitulo, tituloCapitulo)
            self.__capitulos.append(capi)

    def excluirCapitulo(self, tituloCapitulo: str):
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo:
                self.__capitulos.remove(i)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for i in self.__capitulos:
            if i.titulo == tituloCapitulo:
                return i
