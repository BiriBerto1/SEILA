from animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, pode_voar=True):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar
    
    def movimentar(self):
        print('O animal está voando.')
