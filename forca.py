import random


def jogar():

    tela_inicial()
    palavra_secreta = recupera_palavra_secreta()

    enforcou = False
    acertou = False
    erros = 0

    letras_erradas = set()
    letras_certas = ['_' for letra in palavra_secreta]

    # for espacos in palavra_secreta:
    #     letras_certas.append('_')

    while (not enforcou) and (not acertou):
        print(f'Letras erradas: {letras_erradas}')
        print(letras_certas)
        chute = input('Digite uma letra: ')
        index = 0

        chute = chute.strip().upper()

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if letra == chute:
                    letras_certas[index] = chute.upper()
                index += 1
        else:
            letras_erradas.add(chute.upper())
            erros += 1
            print(f'Palavra não tem esta letra. Você ainda tem {6 - erros} tentativas.')

        acertou = '_' not in letras_certas
        enforcou = erros == 6
    
    if acertou:
        print(f'Parabéns! Você descobriu a palavra secreta: {palavra_secreta} em {erros} tentativas.')
    else:
        print(f'Não foi desta vez. Você foi enforcado, a palavra era: {palavra_secreta}')

    print('Fim do jogo!')

def recupera_palavra_secreta():
    arquivo = open('palavras.txt','r')

    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def tela_inicial():
    print('*********************************')
    print('***Bem vindos ao Jogo da Forca***')
    print('*********************************')


# esta verificação deve vir sempre no final do arquivo
if(__name__ == "__main__"):
    jogar()