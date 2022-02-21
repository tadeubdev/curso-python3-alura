from random import randrange

def jogar_adivinhacao():
    print("*************************************")
    print("  Bem vindo ao jogo de adivinhação!  ")
    print("*************************************")

    numero_secreto = randrange(1, 101)
    pontos = 1000

    print("Qual nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "));

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = (numero_secreto == chute)
        maior   = (chute > numero_secreto)
        menor   = (chute < numero_secreto)

        if(acertou):
            print(f"Você acertou! O seu chute foi certeiro!")
            break
        else:
            if(maior):
                print(f"Você errou! O seu chute foi maior que o número secreto: {numero_secreto}!")
            elif(menor):
                print(f"Você errou! O seu chute foi menor que o número secreto: {numero_secreto}")
            # numero secreto - chute
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"Você fez {pontos} pontos!")
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar_adivinhacao()