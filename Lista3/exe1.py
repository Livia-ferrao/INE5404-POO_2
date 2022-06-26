"""Exercício 1. Escreva uma função que conta a frequência de ocorrência de cada palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
"""
# -*- coding: utf-8 -*-
arq = open("file.txt")
txt = arq.readlines()

dic = {}
def contarFrequencia(palavra):
    if palavra in dic.keys():
        dic[palavra] += 1
    else:
        dic[palavra] = 1

for lista in txt:
    lista = lista.split()
    for palavra in lista:
        contarFrequencia(palavra.lower())

print(dic)


