from ave import Ave


class Canarinho(Ave):
    def __init__(self, tamanhoPasso, alturaVoo):
        super().__init__(tamanhoPasso, alturaVoo)
    
    def produzirSom(self):
        frase = "AVE: PRODUZ SOM: PIU"
        return frase

    def cantar(self):
        return self.produzirSom()