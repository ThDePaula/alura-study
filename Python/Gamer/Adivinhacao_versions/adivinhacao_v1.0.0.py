#v1.0.0
print("===================================")
print("Bem-vindo ao jogo de adivinhação!!!")
print("===================================")

numero_secreto = 40

chute = int(input("Digite o seu número: ")) #converte a variável para inteiro

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou, o número é diferente!")

print("Fim de jogo!!")
