import random
import os


jogadas={

'rock':"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

# Paper
'paper':"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",


'scissors':"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",

}





#variável de controle do loop
jogar=True

while jogar:

    print("    Bem vindo ao Jokenpo!      ")
    print("---------------------------------")
    print('\n')


#Pedir que jogador escolha sua jogada
    print('Escolha sua jogada entre as seguintes opções: ')
#Fornecer opções
    print('Pedra: Digite 1')
    print('Papel: Digite 2')
    print('Tesoura: Digite 3')
#Receber input
    escolha=int(input())


#salvar as chaves em uma lista ,permitindo que a jpgaada selecionada seja relacionada as opções do dicionário e gerar uma jogada aleatória para o computador dentro da lista
    lista_jogadas=[]
    for key in jogadas:
        lista_jogadas.append(key)

    jogador=lista_jogadas[escolha-1]
    computador=random.choice(lista_jogadas)

    print(jogadas[jogador])
    print(jogadas[computador])

#Comparar jogada e apontar vencedor
    if jogador=='rock':
        if computador=='rock':
            print('empate')
        elif computador=='paper':
            print('derrota')
        elif computador=='scissors':
            print('vitória')

    elif jogador=='paper':
        if computador=='rock':
            print('vitória')
        elif computador=='paper':
            print('empate')
        elif computador=='scissors':
            print('derrota')

    elif jogador=='scissors':
        if computador=='rock':
            print('derrota')
        elif computador=='paper':
            print('vitória')
        elif computador=='scissors':
            print('empate')


#verificar se o jogador deseja continuar a jogar
    print('Deseja continuar jogado?')
    print('Digite 1 para caso sim.\n')
    print('Digite 2 para caso não.\n')
    encerramento=(input())
    if encerramento=='2':
        jogar=False
    
    os.system('cls')
