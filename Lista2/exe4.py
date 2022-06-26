"""Exercício 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."""

class Vetor:
    def __init__(self, caracteres):
        self.caracteres = caracteres
        self.consoant =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    def consoantes(self):
        soma = 0
        for i in self.caracteres:
            if i in self.consoant:
                print(i)
                soma += 1
        print(f"Consoantes: {soma}")

carc = Vetor(['a', 'b', 'c', '!', 'd', '8', 'j', 'h', 'k', 'g'])
carc.consoantes()