#v2.2.0

import random

print("===================================")
print("Bem-vindo ao jogo de adivinhação!!!")
print("===================================")

numero_secreto = random.randrange(1,101)
total_tentativas = 0
pontuacao = 1000

print("Qual nível dedificuldade deseja?")
print("[1] Fácil\n[2] Médio\n[3] Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for numero_rodada in range(1, total_tentativas + 1):
    print("===================================")
    print("Essa é a sua {} chance de {}".format(numero_rodada, total_tentativas),end="\n\n")

    chute_usuario = int(input("Digite um número de 1 a 100: ")) #converte a variável para inteiro
    print("===================================")

    if(chute_usuario < 1 or chute_usuario > 100 ):
        print("Você deve digitar um número entre 1 a 100. Tente novamente!")
        continue

    acertou     = (chute_usuario == numero_secreto)
    valor_maior = (chute_usuario > numero_secreto)
    valor_menor = (chute_usuario < numero_secreto)

    if(acertou):
        print("Parabéns, você acertou e fez {} pontos!".format(pontuacao))
        break
    else:
        if(valor_maior):
            print("\nVocê errou! Seu chute foi MAIOR que o valor do número secreto!\n")
        elif(valor_menor):
            print("\nVocê errou! Seu chute foi MENOR que o valor do número secreto!\n")
        pontos_perdidos = abs(numero_secreto - chute_usuario) #Caso o chute seja 20 e o número esperdao seja 40 a conta fica (40 - 20 = 20).
        pontuacao = (pontuacao - pontos_perdidos)

print("Fim de jogo!!")
