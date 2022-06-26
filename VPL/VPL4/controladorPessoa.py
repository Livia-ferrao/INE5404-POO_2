from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__todosClientes = []
        self.__todosTecnicos = []

    @property
    def clientes(self):
        return self.__todosClientes
    
    @property
    def tecnicos(self):
        return self.__todosTecnicos

    def incluiCliente(self, codigo: int, nome: str):
        incluido = False
        for i in self.__todosClientes:
            if i.codigo == codigo:
                incluido = True
        if not incluido:
            cliente = Cliente(nome, codigo)
            self.__todosClientes.append(cliente)
            return cliente

    def incluiTecnico(self, codigo: int, nome:str):
        incluido = False
        for i in self.__todosTecnicos:
            if i.codigo == codigo:
                incluido = True
        if not incluido:
            tecnico = Tecnico(nome, codigo)
            self.__todosTecnicos.append(tecnico)
            return tecnico