from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipoChamado = []

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        soma = 0
        for i in self.__chamados:
            if i.tipo.codigo == tipo.codigo:
                soma +=1
        return soma	

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        if isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and isinstance(titulo, str) and isinstance(descricao, str) and isinstance(prioridade, int) and isinstance(tipo, TipoChamado):
            incluido = False
            for i in self.__chamados:
                if (i.data == data) and (i.cliente == cliente) and (i.tecnico == tecnico) and (i.tipo == tipo):
                    incluido = True
            if not incluido:
                chamado =Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
                self.__chamados.append(chamado)
                return chamado
	
    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str):
        incluido = False
        for i in self.__tipoChamado:
            if (i.codigo == codigo):
                incluido = True
        if not incluido:
            tipoChamado = TipoChamado(codigo, descricao, nome)
            self.__tipoChamado.append(tipoChamado)
            return tipoChamado
        
    @property
    def tipoChamados(self):
        return self.__tipoChamado