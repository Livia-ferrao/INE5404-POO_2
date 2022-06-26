"""Exercício 10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

class Vetor:

    def __init__(self, vetor):
        self.vetor = vetor

    def intercalar(v1, v2):
        terceiro = []
        for i in range (0,10):
            terceiro.append(v1.vetor[i])
            terceiro.append(v2.vetor[i])
        print(terceiro)

    
A = Vetor([1,2,3,4,5,6,7,8,9,10])
B = Vetor([1,2,3,4,5,6,7,8,9,10])

Vetor.intercalar(A,B)