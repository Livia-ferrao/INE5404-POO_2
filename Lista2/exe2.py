"""Exercício 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na
ordem inversa.
"""

class Vetor:
    def __init__(self, vetor):
        self.vetor = vetor

    def mostrarInverso(self):
        self.vetor.reverse()
        for i in self.vetor:
            print(i)

    
v1 = Vetor([1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,9.2])
v1.mostrarInverso()