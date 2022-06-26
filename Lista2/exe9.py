"""Exercício 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

class Vetor:
    def __init__(self, vetor):
        self.vetor = vetor
    
    def quadrados(self):
        soma = 0
        for i in self.vetor:
            soma += i*i
        print(soma)
        
A = Vetor([1,2,3,4,5,6,7,8,9,10])
A.quadrados()