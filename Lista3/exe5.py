"""Exercício 6. Criar 10 frozensets com 30 números aleatórios cada, e construir um
dicionário que contenha a soma de cada um deles.
"""

# -*- coding: utf-8 -*-
from random import randint

dic = {}
for i in range(0,10):
    lista = []
    soma = 0
    while len(lista)<30:
        num = randint(0,100)
        if num not in lista:
            lista.append(num)
            soma += num
    fro = frozenset(lista)
    dic[fro] = soma
print(dic)