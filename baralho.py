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

    def total(self, cartas):
        total = 0
        numero_passado = list()
        for c in cartas:
            numero = self.numero(c)
            numero_passado.append(self.numero(c))
            if numero == 11:
                total += 10
            elif numero == 12:
                total += 10
            elif numero == 13:
                total += 10
            elif numero == 1:
                total += 11
            else:
                total += numero
            print(numero_passado)
            if 1 in numero_passado:
                if total > 21:
                    total -= 10
        return total
