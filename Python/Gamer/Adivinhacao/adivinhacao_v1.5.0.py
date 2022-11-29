#v1.5.0

import random

print("===================================")
print("Bem-vindo ao jogo de adivinhação!!!")
print("===================================")

numero_secreto = random.randrange(1,101)
total_tentativas = 3

for numero_rodada in range(1, total_tentativas + 1):
    print("Essa é a sua {} chance de {}".format(numero_rodada, total_tentativas),end="\n\n")

    chute_usuario = int(input("Digite um número de 1 a 100: ")) #converte a variável para inteiro

    if(chute_usuario < 1 or chute_usuario > 100 ):
        print("Você deve digitar um número entre 1 a 100. Tente novamente!")
        continue

    acertou     = (chute_usuario == numero_secreto)
    valor_maior = (chute_usuario > numero_secreto)
    valor_menor = (chute_usuario < numero_secreto)

    if(acertou):
        print("Parabéns, você acertou!")
        break
    else:
        if(valor_maior):
            print("Você errou! Seu chute foi maior que o valor do número secreto!")
        elif(valor_menor):
            print("Você errou! Seu chute foi menor que o valor do número secreto!")

print("Fim de jogo!!")
