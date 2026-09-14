class Neurônio:
    def __init__(self, conexoes: list[int]):
        self.conexoes = conexoes
        self.sucessos = 0
        self.usos = 0
    def sucesso(self):
        self.sucessos += 1
        self.usos += 1
    def falha(self):
        self.usos += 1

class RedeNeural:
    def __init__(self, neurionios: list[Neurônio]):
        self.neuronios = []
    def novo_neuronio(self):
