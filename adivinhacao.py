import random

def jogar():
    print('***********************************')
    print('*Bem vindos ao Jogo de Adivinhação*')
    print('***********************************')

    numero_secreto = random.randint(1,100)
    TENTATIVAS = 0
    PONTOS = 1000

    print('(1) Fácil\n(2) Médio\n(3) Difícil')
    dificuldade = int(input('Digite o nível de dificuldade: '))

    if dificuldade == 1:
        TENTATIVAS = 20
    elif dificuldade == 2:
        TENTATIVAS = 10
    else:
        TENTATIVAS = 5

    for rodada in range(1, TENTATIVAS + 1):
        print(f'Tentativa {rodada} de {TENTATIVAS}')
        chute = int(input('Digite um número entre 1 e 100: '))

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        if(acertou):
            print(f'Você acertou na mosca!\nNúmero Secreto: {numero_secreto}\nchute: {chute}')
            print(f'Você acertou em {rodada} tentativas e somou {PONTOS} pontos.')
            break
        else:
            if maior:
                print(f'Seu chute foi maior que o número informado.\nChute: {chute}')
            elif menor:
                print(f'Seu chute foi menor que o número informado.\nChute: {chute}')
            pontos_perdidos = abs(numero_secreto - chute)
            PONTOS = PONTOS - pontos_perdidos
        

    print(f'Fim do jogo!\nNúmero Secreto: {numero_secreto}')

if(__name__ == "__main__"):
    jogar()
