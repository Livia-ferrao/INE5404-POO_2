"""Exercício 3. Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome.
"""
# -*- coding: utf-8 -*-


def media(nome):
    nota1, nota2 = dic[nome]
    mediaAluno = (nota1 + nota2)/2
    return mediaAluno

dic = {}
while True:
    nome = input()
    if nome == "":
        break
    nota1 = float(input())
    nota2 = float(input())
    dic[nome] = [nota1, nota2]
    print(media(nome))
print(dic)