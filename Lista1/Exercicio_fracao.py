class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.resul = numerador/denominador
        
    def soma(fr1, fr2):
        return fr1.resul + fr2.resul
    
    def sub(fr1, fr2):
        return fr1.resul - fr2.resul
    
    def multi(fr1, fr2):
        return fr1.resul * fr2.resul
    
    def div(fr1, fr2):
        return fr1.resul/fr2.resul
    
    def mostrar(self):
        print(f"{self.numerador}/{self.denominador}")
              
    def inverter(self):
        print(f"{self.denominador}/{self.numerador}")
              
    def valor_real(self):
        print(float(self.resul))
              
    def criar_funcao(num):
        for i in range(2,num+1): 
            if num%i ==0:
                print(f"{int(num*i)}/{i}")
      

f1 = Fracao(5,5)
f2 = Fracao(10,2)
print(Fracao.soma(f1,f2))
print(Fracao.sub(f1,f2))
print(Fracao.multi(f1,f2))
print(Fracao.div(f1,f2))
              
f1.mostrar()
f1.inverter()
f1.valor_real()

Fracao.criar_funcao(4)