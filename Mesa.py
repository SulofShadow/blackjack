from baralho import Baralho


class Mesa(Baralho):
    def __init__(self):
        super(Mesa, self).__init__()
        self.cartas_mesa = list()

# colocar um total depois, pegal j, q, k como 10 e ás com 11 ou 2
    def __str__(self):
        for c in self.cartas_mesa:
            print(self.visual_carta(self.naipe(c), self.numero(c)), end='\t\t\t')
        print('total:',self.total(self.cartas_mesa))

        return ''
