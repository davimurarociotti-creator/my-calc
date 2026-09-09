import random

random_number = random.randint(1, 100)
chances = 0

print("bem vindo ao jogo de adivinhação!")

while chances < 100:
    guess = int(input("Digite um número entre 1 e 100: "))
    chances += 1

    if guess < random_number:
        print("Muito baixo! Tente novamente.")
    elif guess > random_number:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {random_number} em {chances} tentativas.")
        print("Deseja jogar novamente? (s/n)")
        resposta = input().lower()

        if resposta == 'n':
            print("Obrigado por jogar! Até a próxima.")
            break
        elif resposta == 's':
            random_number = random.randint(1, 100)
            chances = 0
            print("Novo jogo iniciado! Boa sorte!")
        else:
            print("Opção inválida. Finalizando jogo.")
            break