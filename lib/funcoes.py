from datetime import datetime
import os
import string
import csv
from random import choice, shuffle


def gerador_senha(tamanho, use_minusculas=False, use_maiusculas=False, use_digitos=False, use_especiais=False):

    pool = ''
    senha = []
    if use_minusculas:
        senha.append(choice(string.ascii_lowercase))
        pool += string.ascii_lowercase
    if use_maiusculas:
        senha.append(choice(string.ascii_uppercase))
        pool += string.ascii_uppercase
    if use_digitos:
        senha.append(choice(string.digits))
        pool += string.digits
    if use_especiais:
        senha.append(choice(string.punctuation))
        pool += string.punctuation
    elif len(pool) == 0:
        return '\33[31mERRO! escolha pelo menos uma opção de caracteres\33[m'

    while len(senha) < tamanho:
        senha.append(choice(pool))

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
            qtd = int(input('Quantas senhas deseja gerar? '))
        except ValueError:
            print('\33[31mErro! Informe um valor válido\33[m')
        else:
            break
    return qtd


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


def salvar_senha(senha):
    """
        Salva uma nova senha no arquivo CSV com as colunas: data, senha e local.
        O campo 'local' inicia vazio e poderá ser editado posteriormente no histórico.
        """
    filename = "senhas_salvas.csv"  # Você pode trocar por "senhas_salvas.txt" se preferir, mas o formato será CSV.
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="", encoding="utf-8") as arquivo:
        fieldnames = ["data", "senha", "local"]
        writer = csv.DictWriter(arquivo, fieldnames=fieldnames) # type: ignore
        if not file_exists:
            writer.writeheader()
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        writer.writerow({"data": timestamp, "senha": senha, "local": ""})
