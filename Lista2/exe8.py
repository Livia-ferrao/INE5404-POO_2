"""Exercício 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""

class Pessoa:
    
    idades = []
    alturas = []

    def __init__(self, idade, altura):
        self.idade = idade
        Pessoa.idades.append(idade)
        self.altura = altura
        Pessoa.alturas.append(altura)
    
    def inverso():
        Pessoa.idades.reverse()
        print(*Pessoa.idades)
        Pessoa.alturas.reverse()
        print(*Pessoa.alturas)
        

    

p1 = Pessoa(30, 1.75)
p2 = Pessoa(20, 2.75)
p3 = Pessoa(10, 1.65)
p4 = Pessoa(15, 1.73)
p5 = Pessoa(19, 1.60)
Pessoa.inverso()