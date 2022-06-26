from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self, volumeSom = 3, tamanhoPasso = 3):
        super().__init__(volumeSom, tamanhoPasso)
    
    def produzirSom(self):
        frase = "MAMIFERO: PRODUZ SOM: "+ str(self.volumeSom)+ " SOM: AU"
        return frase

    def latir(self):
        return self.produzirSom()