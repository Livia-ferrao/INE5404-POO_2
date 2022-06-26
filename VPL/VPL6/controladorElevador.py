from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def subir(self) -> str:
        self.elevador.subir()
    
    def descer(self) -> str:
        self.elevador.descer()

    def entraPessoa(self) -> str:
        self.elevador.entraPessoa()

    def saiPessoa(self) -> str:
        self.elevador.saiPessoa()

    def inicializarElevador(self, andarAtual:int, totalAndaresPredio: int, capacidade: int, totalPessoas: int) -> str:
        if isinstance(andarAtual,int) and isinstance(totalAndaresPredio,int) and isinstance(capacidade, int) and isinstance(totalPessoas,int):
            if andarAtual >= 0 and totalAndaresPredio >=0 and capacidade >=0 and totalPessoas >=0 and andarAtual <= totalAndaresPredio-1 and totalPessoas <= capacidade:
                self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
            else:
                raise ComandoInvalidoException
        else:
            raise ComandoInvalidoException
