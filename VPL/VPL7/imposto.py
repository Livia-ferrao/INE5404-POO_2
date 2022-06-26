from abc import ABC, abstractmethod
from incidencia_imposto import IncidenciaImposto


class Imposto(ABC):
    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        self.__aliquota = aliquota
        self.__incidencia_imposto = incidencia_imposto

    @property
    def aliquota(self):
        return self.__aliquota

    @aliquota.setter
    def aliquota(self, aliquota):
        self.__aliquota = aliquota

    @property
    def incidencia_imposto(self):
        return self.__incidencia_imposto

    @incidencia_imposto.setter
    def incidencia_imposto(self, incidencia_imposto):
        self.__incidencia_imposto = incidencia_imposto

    @abstractmethod
    def calcula_aliquota(self) -> float:
        pass
