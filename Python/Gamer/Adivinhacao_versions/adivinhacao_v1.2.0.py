#v1.2.0
print("===================================")
print("Bem-vindo ao jogo de adivinhação!!!")
print("===================================")

numero_secreto = 40
total_tentativas = 3
numero_rodada = 1

while(numero_rodada <= total_tentativas):
    print("Essa é a sua {} chance de {}".format(numero_rodada, total_tentativas),end="\n\n")

    chute_usuario = int(input("Digite o seu número: ")) #converte a variável para inteiro

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

    numero_rodada = (numero_rodada + 1)

print("Fim de jogo!!")
