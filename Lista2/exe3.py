"""Exercício 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

class Notas:
    def __init__(self, notas):
        self.notas = notas

    def mostrarNotas(self):
        print("Notas:")
        for i in self.notas:
            print(i)
    
    def calcMedia(self):
        tam = len(self.notas)
        soma = 0
        for i in self.notas:
            soma += i
        media = soma/tam
        print(f"Media: {media}")

notas1 = Notas([4,6.8,9,2])
notas1.mostrarNotas()
notas1.calcMedia()