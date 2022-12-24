from baralho import Baralho


class Jogador(Baralho):
    # 1° init é do jogador, e o super é indicando o pai
    def __init__(self, dinheiro):
        super(Jogador, self).__init__()
        self.dinheiro = dinheiro
        self.cartas_mao = list()

    def __str__(self):
        for c in self.cartas_mao:
            print(self.visual_carta(self.naipe(c), self.numero(c)), end='\t\t\t')
        print('total:',self.total(self.cartas_mao))
        return ''
