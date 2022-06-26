"""Exercício 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
class Vetor:
    def __init__(self, vetor):
        self.vetor = vetor
    
    def mostrarVetor(self):
        soma = ""
        for i in self.vetor:
            soma += str(i) + " "
        print(soma)
    
    def soma(self):
        soma = 0
        for i in self.vetor:
            soma += i
        print(soma)

    def multi(self):
        multi = 1
        for i in self.vetor:
            multi *= i
        print(multi)

v1 = Vetor([1,2,3,4,5])
v1.mostrarVetor()
v1.soma()
v1.multi()