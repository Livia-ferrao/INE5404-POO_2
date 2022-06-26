"""Exercício 4. Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O campeão é o que tem a menor média de tempos.
"""
# -*- coding: utf-8 -*-

import operator

menor = 0
vencedor = ""
numvolta = 0

dic = {}
for i in range(0,6): #6 voltas
    nome = input("Nome corredor: ")
    lista = []
    for volta in range(1,11): #10 participantes
        tempo = float(input(f"Tempo da volta {volta}: "))
        lista.append(tempo)
        if i == 0:
            menor = tempo
            vencedor = nome
            numvolta = volta
    dic[nome] = lista

#loop para cada participante
for i in dic:
    soma = 0
    #loop para cada valor na lista de tempo
    for num in range(0, len(dic[i])):
        if dic[i][num] < menor:
            menor = dic[i][num]
            numvolta = num + 1
            vencedor = i
        soma += dic[i][num]
    media = soma / 10
    dic[i] = media

print(f"{vencedor} fez o menor tempo de {menor} em sua {numvolta}° volta")

novodic = sorted(dic.items(), key=operator.itemgetter(1))

#variável cotadora
c = 0
for tupla in novodic:
    lista = list(tupla)
    c +=1
    print(f"{c}° lugar: {lista[0]} - {lista[1]} segundos")

