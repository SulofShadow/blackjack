from baralho import Baralho
from Mesa import Mesa
from Jogador import Jogador
from time import sleep


dinheiro_apostado = int(input('Quanto que vai querer jogar? R$'))

jogador = Jogador(dinheiro_apostado)
mesa = Mesa()
baralho = Baralho()

baralho.dar_cartas(mesa.cartas_mesa)

baralho.dar_cartas(jogador.cartas_mao)
baralho.dar_cartas(jogador.cartas_mao)

dinheiro_rodada = int(input('Vai apostar quanto? R$'))

print("""
____________________________________
|⢰⡶⣆⠀⠀⠀⠀⣰⢶⡆⠀⢰⡶⠶⠶⠖⠀⢠⡶⠞⠶⡆⠀⠀⠀⣴⣶⠀⠀⠀ |
|⢸⡇⢻⡄⠀⠀⢠⡟⢸⡇⠀⢸⡇⠀⠀⠀⠀⢺⣇⠀⠀⠀⠀⠀⢰⡏⢹⣇⠀⠀ |
|⢸⡇⠈⣷⡀⢀⡾⠀⢸⡇⠀⢸⡟⠛⠛⠃⠀⠀⠙⠿⣦⡄⢀⣿⠀⠀⢿⡄ ⠀|
|⢸⡇⠀⠸⣧⣼⠃ ⢸⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⣸⠟⠛⠛⠻⣧⠀ |
|⠸⠇⠀⠀⠻⠏⠀⠀⠸⠇⠀⠸⠷⠶⠶⠶⠀⠻⠶⠶⠞⠃⠠⠟⠀⠀⠀⠀⠹⠆ |
-------------------------------------
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
print(mesa)

print("""
___________________________________
|⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |   
|    ⢀⣀⠀⠀⠀⠀⢀⣀⠀⠀⠈⢀⣉⠉⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀   |
|    ⢸⠻⡇⠀⠀⢀⡿⣿⠀⠀⠀⡼⢹⡆⠀⠀⢰⡏⠀⠀⠈⣷⠀    |
|    ⢸⠀⢻⡄⠀⡼⠁⣿⠀⠀⢸⠇⠀⢿⡀⠀⣿⠀⠀⠀⠀⢸⡇⠀   |
|    ⢸⠀⠈⣷⣼⠇⠀⣿⠀⢀⡟⠛⠛⠛⣇⠀⢹⣆⠀⠀⢀⣾⠀⠀   |
|    ⠘⠀⠀⠘⠋⠀⠀⠛⠀⠚⠁⠀⠀⠀⠙⠂⠀⠙⠓⠒⠛⠁⠀⠀⠀⠀ |
-----------------------------------
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
print(jogador)

#
#
#
#                                               AJEITAR ESSA PARTE
#
#
#
perdeu = False

while not perdeu:
    escolha_menu = ''

    while escolha_menu not in [1, 2, 3, 4]:
        escolha_menu = int(input('Ⅰ- mais uma\tⅡ- Manter\nⅢ- Dobra\t\tⅣ- Dividir\n'))

    if escolha_menu == 1:
        baralho.dar_cartas(jogador.cartas_mao)
        print(jogador)
    if escolha_menu == 2:
        while mesa.total(mesa.cartas_mesa) < 17:
            baralho.dar_cartas(mesa.cartas_mesa)
            print(mesa)
            sleep(1)

    # if escolha_menu == 3:
    #     jogador.dobrar()
    # if escolha_menu == 4:
    #     jogador.dividir()

    if jogador.total(jogador.cartas_mao) > 21 or mesa.total(mesa.cartas_mesa) > jogador.total(jogador.cartas_mao):
        perdeu = True
        print('perdeu')
    if jogador.total(jogador.cartas_mao) == mesa.total(mesa.cartas_mesa):
        print('empate')
    else:
        print('ganhou')
        break
#
#
#
#
#
#
# 
