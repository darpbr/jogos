import forca
import adivinhacao

def escolha_jogo():
    print('*********************************')
    print('********Escolha sesu jogo********')
    print('*********************************')

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Digite sua opção: '))

    if jogo == 1:
        print('Jogo da Forca selecionado!')
        forca.jogar()
    else:
        print('Jogo de Advinhação selecionado!')
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()
