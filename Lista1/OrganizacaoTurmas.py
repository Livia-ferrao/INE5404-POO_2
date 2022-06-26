"""Organização das Turmas
Crie um sistema que gerencia o cadastro de alunos e professores em turmas. Os usuários
serão os membros da secretaria. Eles devem conseguir visualizar os alunos matriculados em
cada turma, com seus dados, suas notas e presenças. Além disso, os secretários precisam ter
acesso a dados cadastrais dos professores associados à disciplina.

SOLUÇÃO: Aloca-se alunos com seu professor, o qual ja esta definido todas turmas que da aula. Verifica-se, também, dados gerais dos estudantes e professores."""

class Turma:
    def __init__(self, alunos, professor):
        self.alunos = alunos
        self.professor = professor

    def dados(self):
        print(f"Dados dos alunos: ")
        for i in self.alunos:
            print(f"{i.nome} - {i.matricula} - {i.nota} - {i.presenca}")
        print(f"Dados do professor: {self.professor.nome}\n")

class Aluno:
    def __init__(self, nome, matricula, nota, presenca):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        self.presenca = presenca

class Professor:
     def __init__(self, nome, turmas):
        self.nome = nome
        self.turma = turmas

a1 = Aluno("Matheus", 2, 10.0, "70%")
a2 = Aluno("Carlos", 3, 9.0, "60%")
a3 = Aluno("Paulo", 4, 4.0, "50%")
a4 = Aluno("Pedro", 5, 6.0, "40%")

p1 = Professor("José", [302, 301, 303, 304])
p2 = Professor("João", [302, 301, 303, 304])

turma1 = Turma([a1,a2], p1)
turma1.dados()
turma2 = Turma([a3,a4], p2)
turma2.dados()