print('*' * 43)
print('            JOGO DA FORCA            ')
print('*' * 43)

from random import choice

vocabulario = ["verde", "amarelo", "roxo", "branco", "preto", "azul",
               "elefante", "girafa", "cachorro", "gato", "rinoceronte",
               "melancia", "laranja", "goiaba", "framboesa", "banana"]

palavra = choice(vocabulario)

alfabeto = list('abcdefghijklmnopqrstuvwxyz')
tentativas = []
chances = 7
errou_palpite = []

cor = ["verde", "amarelo", "roxo", "branco", "preto", "azul"]
animal = ["elefante", "girafa", "cachorro", "gato", "rinoceronte"]
fruta = ["melancia", "laranja", "goiaba", "framboesa", "banana"]

if palavra in cor:
    print("")
    print("A dica da palavra é: COR")

elif palavra in animal:
    print("")
    print("A dica da palavra é: ANIMAL")

elif palavra in fruta:
    print("")
    print("A dica da palavra é: FRUTA")

# DIGITANDO O PALPITE E EXCLUINDO CONDIÇOES ADVERSAS______________________________________
while True:
    palpite = input(
        "\nDigite uma letra ou 'SAIR' para sair do programa:").lower()  # lower para manter tudo que o usuario preencher minusculo
    if palpite == "sair":
        break

    elif palpite not in alfabeto or palpite == '':
        print('Desculpe, isso não é valido, digite uma letra do alfabeto....')
        continue

    elif palpite in tentativas:
        print("Letra já utilizada, tente outra....")
        continue

    tentativas.append(palpite)  # Append: A celula "tentativa" sempre receberá a letra palpitada.
    if palpite in palavra:
        print("Acertou a letra!")
        print('')
        for letra in palavra:
            if letra in tentativas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

    else:
        print('Errou a(s) letra(s)!')
        errou_palpite.append(palpite)
        print(errou_palpite)
        if chances == 7:
            print("-----|")
            print('')
        if chances == 6:
            print("-----|")
            print("     O")
            print('')
        if chances == 5:
            print("-----|")
            print("     O")
            print("     |")
            print('')
        if chances == 4:
            print("-----|")
            print("     O")
            print("    /|")
            print('')
        if chances == 3:
            print("-----|")
            print("     O")
            print("    /|\ ")
            print('')
        if chances == 2:
            print("-----|")
            print("     O")
            print("    /|\ ")
            print("    / ")
            print('')
        for letra in palavra:
            if letra in tentativas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        chances -= 1

    if chances == 0:
        print('')
        print("-----|")
        print("     O")
        print("    /|\ ")
        print("    / \ ")
        print('')
        print("Fim de jogo, GAME OVER")
        print('A palavra era', palavra.upper(), "!")
        break

    elif set(palavra).issubset(set(tentativas)):
        print(": Parabéns, você acertou!")
        print('')
        print("     -------------              _\|/_                   ")
        print("    /------------ \             -/|\-                   ")
        print("   |               |               .                    ")
        print(" / |      /|       | \              .                   ")
        print("|  |       |       |  |            .                   ")
        print(" \ _\     ---     /_ /           .                      ")
        print("     \           /                .                     ")
        print("      \         /                   .                   ")
        print("        ______                     .                   ")
        print("      /________\                   .                    ")
        break



