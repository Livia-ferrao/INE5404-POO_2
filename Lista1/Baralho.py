"""Projete e implemente um baralho de cartas genérico, isto é, que poderia ser usado para
implementar diversos jogos de carta.

SOLUÇÃO: Baralho tradicional de 52 cartas, não englobando baralhos específicos, o qual tem função de mostrar todas as cartas do baralho e as baralhar. """

class Carta:
    def __init__(self, naipe=0, valor=2):
        self.naipe = naipe
        self.valor = valor
        self.naipes = ["Paus","Ouros","Copas","Espadas"]
        self.valores= [".", "Ás", "2", "3", "4", "5","6", "7", "8", "9", "10","Valete", "Rainha", "Rei"]

    def __str__(self):
        return (f"{self.valores[self.valor]} de {self.naipes[self.naipe]}")

class Baralho:
    def __init__(self):
        self.cartas = []
        for n in range(0,4): # naipes de 0 a 3
            for v in range(1,14): # valores de 1 a 13
                self.cartas.append(Carta(n,v))
        #print(self.cartas)
    def __str__(self):
        cartas = ""
        for i in range(0, len(self.cartas)):
            cartas += str(self.cartas[i]) + "\n"
        return cartas

    def embaralhar(self):
        import random
        for i in range(0, len(self.cartas)):
            carta_aleatoria = random.randint(0, len(self.cartas)-1)
            aux = self.cartas[i]
            self.cartas[i] = self.cartas[carta_aleatoria]
            self.cartas[carta_aleatoria] = aux
    
    def darCartas(self, jogadores, qntdCartas):
        for jog in range(0, jogadores):
            for i in range(0, qntdCartas):
                self.cartas.pop()



carta1 = Carta(0,10)
carta2 = Carta(0,4)

baralho1 = Baralho()
print(baralho1.cartas)
baralho1.embaralhar()
print(len(baralho1.cartas))
print(baralho1)

baralho1.darCartas(2, 5)
print()
print(len(baralho1.cartas))
    