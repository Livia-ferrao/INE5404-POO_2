from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):

    def __init__(self, nome: str):
        self.__nome = nome
        self.__cartasMao = []

    @property
    def nome(self) -> str:
        return self.__nome

    def baixa_carta_da_mao(self) -> Carta:
        carta = random.choice(self.__cartasMao)
        self.__cartasMao.remove(carta)
        return carta

    @property
    def mao(self) -> list:
        return self.__cartasMao

    def inclui_carta_na_mao(self, carta: Carta):
        if type(carta) is Carta:
            self.__cartasMao.append(carta)
