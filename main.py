from baralho import Baralho
from Mesa import Mesa
from Jogador import Jogador


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
------------------------------------|
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

escolha_menu = ''
while escolha_menu not in [1,2,3,4]:
    escolha_menu = int(input('Ⅰ- Pede mais uma\nⅡ- Dobra\nⅢ- Ver mão\nⅣ- Ver mesa\n'))

if escolha_menu == 1:
    baralho.dar_cartas(jogador.cartas_mao)
if escolha_menu == 2:
    baralho.dar_cartas(jogador.cartas_mao)
    dinheiro_rodada *= 2
if escolha_menu == 3:
    print(jogador)
if escolha_menu == 4:
    print(mesa)