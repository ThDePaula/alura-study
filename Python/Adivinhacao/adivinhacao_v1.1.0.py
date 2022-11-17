#v1.1.0
print("===================================")
print("Bem-vindo ao jogo de adivinhação!!!")
print("===================================")

numero_secreto = 40

chute_usuario = int(input("Digite o seu número: ")) #converte a variável para inteiro

acertou     = (chute_usuario == numero_secreto)
valor_maior = (chute_usuario > numero_secreto)
valor_menor = (chute_usuario < numero_secreto)

if(acertou):
    print("Parabéns, você acertou!")
else:
    if(valor_maior):
        print("Você errou! Seu chute foi maior que o valor do número secreto!")
    elif(valor_menor):
        print("Você errou! Seu chute foi menor que o valor do número secreto!")
#print("Você errou, o número é diferente!")

print("Fim de jogo!!")
