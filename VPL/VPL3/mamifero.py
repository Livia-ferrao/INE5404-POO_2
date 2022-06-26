from abc import ABC, abstractmethod
from animal import Animal


class Mamifero(Animal, ABC): 
    def __init__(self, volumeSom: int, tamanho_passo: int):
        super().__init__(tamanho_passo)
        self.__volumeSom = volumeSom

    @property
    def volumeSom(self):
        return self.__volumeSom
    
    @volumeSom.setter
    def volumeSom(self, volumeSom):
        self.__volumeSom = volumeSom
    
    @abstractmethod
    def produzirSom(self):
        pass