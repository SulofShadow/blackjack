from baralho import Baralho


class Mesa(Baralho):
    def __init__(self):
        super(Mesa, self).__init__()
        self.cartas_mesa = list()

    def __str__(self):
        for c in self.cartas_mesa:
            print(self.visual_carta(self.naipe(c), self.numero(c)), end='\t\t\t')
        print('total:', self.total(self.cartas_mesa))

        return ''
