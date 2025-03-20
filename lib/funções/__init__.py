from datetime import datetime
import os

def gerador_senha(tamanho, use_minusculas=False, use_maiusculas=False, use_digitos=False, use_especiais=False):
    import string
    from random import choice

    caracteres = ''
    if use_minusculas:
        caracteres += string.ascii_lowercase
    if use_maiusculas:
        caracteres += string.ascii_uppercase
    if use_digitos:
        caracteres += string.digits
    if use_especiais:
        caracteres += string.punctuation
    elif len(caracteres) == 0:
        return '\33[31mERRO! escolha pelo menos uma opção de caracteres\33[m'

    senha = ''.join(choice(caracteres) for _ in range(tamanho))
    return senha


def comprimento():
    while True:
        try:
            tamanho = int(input('Diga o comprimento da senha (mínimo 6 caracteres): '))
            if tamanho < 6:
                print('\33[31mErro: A senha deve ter no mínimo 6 caracteres.\33[m')
            else:
                break
        except:
            print('\33[31mDigite um valor válido!\33[m')
    return tamanho


def quantidade():
    while True:
        try:
            quantidade = int(input('Quantas senhas deseja gerar? '))
        except:
            print('\33[31mErro! Informe um valor válido\33[m')
        else:
            break
    return quantidade


def caracteres():
    especiais = input('Incluir caracteres especiais? (S/N): ').upper().strip() == 'S'
    minusculas = input('Incluir letras minúsculas? (S/N): ').upper().strip() == 'S'
    maiusculas = input('Incluir letras maiusculas? (S/N): ').upper().strip() == 'S'
    digitos = input('Incluir digitos? (S/N): ').upper().strip() == 'S'
    print('-' * 75)
    return minusculas, maiusculas, digitos, especiais


def opc1(tamanho, minusculas, maiusculas, digitos, especiais):
    senha = gerador_senha(tamanho, minusculas, maiusculas, digitos, especiais)
    return senha


def opc2():
    qtd = quantidade()
    tamanho = comprimento()
    minusculas, maiusculas, digitos, especiais = caracteres()

    senhas = []
    for _ in range(qtd):
        senha = opc1(tamanho, minusculas, maiusculas, digitos, especiais)
        senhas.append(senha)
        print('Senha gerada:', senha)

    return senhas


def CriarCadastrar(nome, senhas):
    modo = 'a' if os.path.exists(nome) else 'w'
    with open(nome, modo) as arquivo:
        for senha in senhas:
            timestamp = datetime.now().strftime('%A, %d %B %Y %H:%M:%S')
            arquivo.write(f'{timestamp} - {senha}\n')