import adivinhacao
import forca

print("===============================")
print("Seja bem vindo! Escolha um jogo")
print("===============================")

print("[1] Adivinhação\n[2] Forca\n")

jogo = int(input("Qual sua escolha? "))

if(jogo == 1):
    print("Jogando o jogo da Adivinhação!!\n")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogango o jogo da Forca!!\n")
    forca.jogar()
else:
    print("Escolha um jogo!")