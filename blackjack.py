import random


class Baralho:
    def __init__(self):
        self.jogo = list()

    def __str__(self):
        return (self.visual_carta(self.naipe(self.jogo[-1]), self.numero(self.jogo[-1])))

    def dar_cartas(self):
        carta = random.randint(1, 53)
        if carta not in self.jogo:
            self.jogo.append(carta)
            print(carta)

    def naipe(self, numero_carta):
        if numero_carta < 14 and numero_carta > 0:
            return "♣"
        if numero_carta < 27 and numero_carta > 13:
            return "♦"
        if numero_carta < 40 and numero_carta > 26:
            return "♥"
        if numero_carta < 53 and numero_carta > 39:
            return "♠"

    def numero(self, numero):
        if numero < 14:
            return numero
        else:
            while numero >= 14:
                numero -= 13
            return numero

    def visual_carta(self, naipe, numero):
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
                            _________
                            |{numero}      |
                            |{naipe}      |
                            |   {naipe}   |
                            |      {numero}|
                            |      {naipe}|
                            ---------"""

        else:
            a = f"""
                            ________
                            |{numero}     |
                            |{naipe}      |
                            |   {naipe}   |
                            |     {numero}|
                            |      {naipe}|
                            --------"""

        return a


baralho = Baralho()
baralho.dar_cartas()
print(baralho)

