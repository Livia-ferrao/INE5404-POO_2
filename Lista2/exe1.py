"""Exercício 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

class Vetor:
    def __init__(self, vetor):
        self.vetor = vetor
    
    def mostrarVetor(self):
        for i in self.vetor:
            print(i)

v1 = Vetor([1,2,3,4,5])
v1.mostrarVetor()