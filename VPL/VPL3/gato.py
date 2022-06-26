from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self, tamanhoPasso =2, volumeSom=2):
        super().__init__(volumeSom, tamanhoPasso)

    def produzirSom(self):
        frase = "MAMIFERO: PRODUZ SOM: "+ str(self.volumeSom)+ " SOM: MIAU"
        return frase
    
    def miar(self):
        return self.produzirSom()