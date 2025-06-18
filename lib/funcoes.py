from datetime import datetime
import os
import string
from random import choice, shuffle

def gerador_senha(tamanho, use_minusculas=False, use_maiusculas=False, use_digitos=False, use_especiais=False):

    caracteres = ''
    senha = []
    if use_minusculas:
        senha.append(choice(string.ascii_lowercase))
        caracteres += string.ascii_lowercase
    if use_maiusculas:
        senha.append(choice(string.ascii_uppercase))
        caracteres += string.ascii_uppercase
    if use_digitos:
        senha.append(choice(string.digits))
        caracteres += string.digits
    if use_especiais:
        senha.append(choice(string.punctuation))
        caracteres += string.punctuation
    elif len(caracteres) == 0:
        return '\33[31mERRO! escolha pelo menos uma opção de caracteres\33[m'

    while len(senha) < tamanho:
        senha.append(choice(caracteres))

    shuffle(senha)
    return ''.join(senha)

    
# Para a interface, talvez você deseje uma função simples que retorne o valor do Entry.  
# Caso mantenha para CLI, adapte-o para que não use input() e sim valide um valor recebido.
# Aqui só deixamos como exemplo, se for usado no CLI.
def comprimento():
        
    try:
        tamanho = int(input('Diga o comprimento da senha (mínimo 6 caracteres): '))
        if tamanho < 6:
            print('\33[31mErro: A senha deve ter no mínimo 6 caracteres.\33[m')
            return None
        return tamanho
    except (ValueError, TypeError):
        print('\33[31mDigite um valor válido!\33[m')
        return None


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


def salvar_senha(senhas):
    
    with open("senhas_salvas.txt", "a") as arquivo:
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f'{timestamp} - {senhas}\n')