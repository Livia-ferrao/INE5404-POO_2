"""O banco Tatu, moderno e eficiente, precisa de um novo programa para controlar o saldo de
seus correntistas. Cada conta corrente pode ter um ou mais clientes como titular. O banco
controla apenas o nome e o telefone de cada cliente. A conta corrente apresenta um saldo e
uma lista de operações de saques e depósitos. Quando o cliente fizer um saque, diminuiremos
o saldo da conta corrente. Quando ele fizer um depósito, aumentaremos o saldo.O banco oferece também contas especiais, com limite especial além do saldo, e conta poupança, que oferece um rendimento mensal sempre que o saldo na conta completa um mês. Evidentemente é necessário oferecer aos clientes a possibilidade de verificar saldos, extratos e um resumo com todas as informações da conta e seus respectivos clientes.

SOLUÇÃO: Função de cadastrar clientes e atribuir tipos de contas, cada uma com suas funções específicas.
"""

class Cliente:
    def __init__(self, nome, tel):
        self.nome = nome
        self.tel = tel


class ContaCorrente:
    def __init__(self, clientes, num, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.operacoes = []
        self.num = num

    def saque(self, valor):
        if self.saldo > 0:
            self.saldo -= valor
            self.operacoes.append("SAQUE")
            self.operacoes.append(valor)
        else:
            print("Operação não realizada")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append("DEPÓSITO")
        self.operacoes.append(valor)

    def verificarSaldo(self):
        print(self.saldo)

    def extrato(self):
        for i in range(1, len(self.operacoes),2):
            print(f"{self.operacoes[i-1]} - {self.operacoes[i]} ")

    def resumo(self):
        print(f"Número da conta: {self.num}")
        print(f"Saldo: {self.saldo}")
        for i in range(0, len(self.clientes)):
            print(f"Cliente: {self.clientes[i].nome} - Telefone: {self.clientes[i].tel}")

class ContaEspecial(ContaCorrente):
    def __init__(self, clientes, num, saldo=0, limite=0):
        ContaCorrente.__init__(self, clientes, num, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite > 0:
            self.saldo -= valor
            self.operacoes.append("SAQUE")
            self.operacoes.append(valor)

    def extrato(self):
        ContaCorrente.extrato(self)
        print(f"Limite: {self.limite}")
        print(f"Conta atual: {self.limite + self.saldo}")


class ContaPoupanca(ContaCorrente):
    def __init__(self, clientes, num, saldo=0):
        ContaCorrente.__init__(self, clientes, num, saldo)

    def aplicar_rendimento(self):
        rendimento = 0.3
        conta_rendimento = self.saldo * rendimento


cliente1 = Cliente("Pedro", 3847329384)
cliente2 = Cliente("Paulo", 9767325444)

c1 = ContaCorrente([cliente1, cliente2], 345654, 50)
c1.saque(8)
c1.saque(60)
c1.deposito(10)
c1.resumo()
c1.extrato()

c2 = ContaEspecial([cliente1], 34534, 30, 20)
c2.saque(10)
c2.resumo()
c2.extrato()

c3 = ContaPoupanca([cliente1], 34534, 30)
c3.aplicar_rendimento()
c3.resumo()
c3.extrato()
