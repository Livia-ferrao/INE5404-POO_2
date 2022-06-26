from random import randint

dic = {}
for i in range(0,10):
    lista =[]
    soma = 0
    while len(lista)<30:
        valor = randint(0,1000)
        if valor not in lista:
            lista.append(valor)
            soma+= valor
    fr1 = frozenset(lista)
    dic[fr1] = soma
print(dic)
    
