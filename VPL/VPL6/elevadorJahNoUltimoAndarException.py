class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        super().__init__("Elevador ja esta no ultimo andar")