from adivinhacao import jogar_adivinhacao
from forca import jogar_forca

print("*****************************************")
print("  Bem vindo à nossa arena de jogos!      ")
print("*****************************************")


def start():
    print("\nTemos os seguintes jogos:")
    print("(1) Adivinhacao (2) Forca")

    jogo = int(input("Qual jogo você gostaria? "))

    if (jogo < 1 or jogo > 2):
        print("Esse jogo não foi encontrado!\n")
        start()
        return

    print("\n")

    if (jogo == 1):
        jogar_adivinhacao()
    elif (jogo == 2):
        jogar_forca()


if (__name__ == "__main__"):
    start()
