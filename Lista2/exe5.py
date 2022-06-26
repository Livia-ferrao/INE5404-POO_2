"""Exercício 5. Faça um Programa que leia 20 números inteiros e armazene-os num
vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor
impar. Imprima os três vetores.
"""
class Numeros:
    def __init__(self, nums):
        self.nums = nums
        self.par =[]
        self.impar =[]
    
    def parOuImpar(self):
        for i in self.nums:
            if i%2==0:
                self.par.append(i)
            else:
                self.impar.append(i)

    def mostrarNums(self):
        print("Numeros: ")
        for i in range(0,len(self.nums)):
            if i == len(self.nums)-1:
                print(self.nums[i])
            else:
                print(self.nums[i], end=' ')
        
        print("Numeros impares: ")
        impares = ""
        for i in self.impar:
            impares += str(i) + " "
        print(impares)

        print("Numeros pares: ")
        pares = ""
        for i in self.par:
            pares += str(i) + " "
        print(pares)

num =Numeros([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
num.parOuImpar()
num.mostrarNums()