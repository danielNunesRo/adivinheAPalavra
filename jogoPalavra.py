
palavra_secreta = 'fortunamajor'
letras_acertadas = ''
cont = 0
while True:
    letra = input('Digite uma letra: ').lower()
    cont += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada+= '*'
    print(palavra_formada)

    print(f'Tentativas: {cont}')

    if palavra_formada == palavra_secreta:

        print('Você ganhou, parabéns !!!!')
        print(f'A palavra era, {palavra_secreta}')
        break






