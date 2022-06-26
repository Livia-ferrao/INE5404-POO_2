"""Reimplemente o jogo da forca completamente orientado a objetos

SOLUÇÃO: Jogo da forca em que a palavra chave é cadastrada e as tentativas também. Jogo padrão com 6 tenativas até perder."""
class JogoForca:
    def __init__(self, palavra_certa):
        self.palavra_certa = palavra_certa
        self.chances = 5
        self.tentativas = []

    def tentativa(self, tentativa):
        if tentativa == self.palavra_certa:
            print(f"Ganhou! Parabéns")
        elif self.chances ==0:
            print(f"Você perdeu!")
        else:
            if tentativa in self.tentativas:
                print("Esta letra já foi, tente outra!")
            elif tentativa in self.palavra_certa:
                print("Está letra tem na palavra certa!")
                self.tentativas.append(tentativa)
                self.chances -=1
            elif tentativa not in self.palavra_certa:
                print("Errou! Esta letra não está na palavra certa!")
                self.tentativas.append(tentativa)
                self.chances -=1

        #print(self.chances) #apenas para teste
                    
            
t1 = JogoForca("amarelo")
t1.tentativa("a")
t1.tentativa("y")
t1.tentativa("y")
t1.tentativa("m")
t1.tentativa("amarelo")

t2 = JogoForca("azul")
t2.tentativa("a")
t2.tentativa("z")
t2.tentativa("u")
t2.tentativa("azul")

t2 = JogoForca("carro")
t2.tentativa("b")
t2.tentativa("d")
t2.tentativa("f")
t2.tentativa("t")
t2.tentativa("o")
t2.tentativa("c")
