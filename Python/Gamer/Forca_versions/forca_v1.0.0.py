def jogar():
    print("===========================")
    print("Bem vindo ao jogo da Forca!")
    print("===========================")

    palavra_secreta = "banana"
    
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ").lower().strip()
        # .lower() --> deixa tudo minúsculo
        # .strip() --> retira os espaço antes e depois da palavra
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Existe a letra {} na posição {}".format(chute, index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

#Caso o arquivo seja chamado diretamente irá chamar a função.
if(__name__ == "__main__"):
    jogar()