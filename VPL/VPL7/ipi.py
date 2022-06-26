from xmlrpc.client import boolean
from imposto import Imposto
from incidencia_imposto import IncidenciaImposto

'''
O calculo da Aliquota do IPI (percentual do imposto) leva em conta
se existe "aliquota_adicional".
Se existir aliquota_adicional, a aliquota e aumentada em 10%.
Por exemplo, se a aliquota informada no construtor for 10.0
e existe "aliquota_adicional", entao a aliquota calculada sera de 11.0.
'''


class IPI(Imposto):
    def __init__(self, aliquota: float,
                 incidencia_imposto: IncidenciaImposto,
                 aliquota_adicional: boolean):
        super().__init__(aliquota, incidencia_imposto)
        self.__aliquota_adicional = aliquota_adicional

    def calcula_aliquota(self):
        if self.__aliquota_adicional:
            aliquota = self.aliquota + (self.aliquota * 0.1)
        return aliquota
