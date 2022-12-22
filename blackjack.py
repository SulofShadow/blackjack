import random


class Baralho:
    def __init__(self):
        self.cartas_jogadas = list()

    def dar_cartas(self, onde):
        carta = random.randint(1, 52)
        while carta in self.cartas_jogadas:
            carta = random.randint(1, 52)
        self.cartas_jogadas.append(carta)
        onde.append(carta)

    @staticmethod
    def naipe(numero_carta):
        if 14 > numero_carta > 0:
            return "♣"
        if 27 > numero_carta > 13:
            return "♦"
        if 40 > numero_carta > 26:
            return "♥"
        if 53 > numero_carta > 39:
            return "♠"

    @staticmethod
    def numero(numero):
        if numero < 14:
            return numero
        else:
            while numero >= 14:
                numero -= 13
            return numero

    @staticmethod
    def visual_carta(naipe, numero):
        if numero == 1:
            numero = "A"
        if numero == 11:
            numero = "J"
        if numero == 12:
            numero = "Q"
        if numero == 13:
            numero = "K"

        if numero != 10:
            a = f""" 
                            __________
                            |{numero}       |
                            |{naipe}      |
                            |   {naipe}   |
                            |       {numero}|
                            |      {naipe}|
                            ----------"""

        else:
            a = f"""        
                            __________
                            |{numero}      |
                            |{naipe}      |
                            |   {naipe}   |
                            |      {numero}|
                            |      {naipe}|
                            ----------"""

        return a


class Jogador(Baralho):

    # 1° init é do jogador, e o super é indicando o pai
    def __init__(self, dinheiro):
        super(Jogador, self).__init__()
        self.dinheiro = dinheiro
        self.cartas_mao = list()

    def __str__(self):
        for c in self.cartas_mao:
            print(self.visual_carta(self.naipe(c), self.numero(c)), end=' ')
        return ''


class Mesa(Baralho):
    def __init__(self):
        super(Mesa, self).__init__()
        self.cartas_mesa = list()

    def __str__(self):
        for c in self.cartas_mesa:
            print(self.visual_carta(self.naipe(c), self.numero(c)), end=' ')
        return ''


joao = Jogador(500)
mesa = Mesa()
baralho = Baralho()

baralho.dar_cartas(joao.cartas_mao)
baralho.dar_cartas(joao.cartas_mao)

baralho.dar_cartas(mesa.cartas_mesa)
baralho.dar_cartas(mesa.cartas_mesa)

print('MESA')
print(mesa)
print('JOGADOR')
print(joao)


print(baralho.cartas_jogadas)
