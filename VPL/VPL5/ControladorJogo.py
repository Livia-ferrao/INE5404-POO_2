from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        if type((energia and
                 habilidade and
                 velocidade and
                 resistencia) is int) and type(tipo) is Tipo:
            novo = Personagem(energia,
                              habilidade,
                              velocidade,
                              resistencia,
                              tipo)
            self.__personagens.append(novo)
            return novo

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if type(personagem) is Personagem:
            novo = Carta(personagem)
            self.__baralho.append(novo)
            return novo

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        if type(jogador1 and jogador2) is Jogador:
            for i in range(0, 5):
                carta1 = random.choice(self.__baralho)
                carta2 = random.choice(self.__baralho)
                jogador1.inclui_carta_na_mao(carta1)
                jogador2.inclui_carta_na_mao(carta2)
                self.__baralho.remove(carta1)
                self.__baralho.remove(carta2)

    def jogada(self, mesa: Mesa) -> Jogador:
        if type(mesa) is Mesa:
            cartaJog1 = mesa.carta_jogador1
            cartaJog2 = mesa.carta_jogador2
            jog1 = mesa.jogador1
            jog2 = mesa.jogador2
            totCarta1 = cartaJog1.valor_total_carta()
            totCarta2 = cartaJog2.valor_total_carta()

        if totCarta1 > totCarta2:
            jog1.inclui_carta_na_mao(cartaJog1)
            jog1.inclui_carta_na_mao(cartaJog2)
        elif totCarta1 < totCarta2:
            jog2.inclui_carta_na_mao(cartaJog1)
            jog2.inclui_carta_na_mao(cartaJog2)
        else:
            jog1.inclui_carta_na_mao(cartaJog1)
            jog2.inclui_carta_na_mao(cartaJog2)

        if len(mesa.jogador1.mao) == 0:
                return jog2
        elif len(mesa.jogador2.mao) == 0:
                return jog1
        return None
