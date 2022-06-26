"""Exercício 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

class Aluno:
    todasMedias = []

    def __init__(self, notas):
        self.notas = notas
        self.medias = []

    def media(self):
        soma = 0
        tam = len(self.notas)
        for i in self.notas:
            soma += i
        media = soma/tam
        Aluno.todasMedias.append(media)

    def aprovados():
        soma = 0
        for i in Aluno.todasMedias:
            if i>=7:
                soma+=1
        print(f"Numero de alunos com nota maior que 7: {soma}")

    


a1 = Aluno([4,5,6,2])
a2 = Aluno([7,5.5,6.4,9.1])
a3 = Aluno([1,5,9,7])
a4 = Aluno([2,5.3,10,1.2])
a5 = Aluno([8,2,6,9])
a6 = Aluno([2,4,10,9])
a7 = Aluno([10,10,10,10])
a8 = Aluno([6,10,5,9])
a9 = Aluno([9,10,6,7])
a10 = Aluno([8,5,7,9])

a1.media()
a2.media()
a3.media()
a4.media()
a5.media()
a6.media()
a7.media()
a8.media()
a9.media()
a10.media()
print(Aluno.todasMedias)

Aluno.aprovados()