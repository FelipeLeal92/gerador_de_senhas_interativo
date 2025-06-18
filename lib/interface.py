from datetime import datetime
import os

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\33[31mERRO: Por favor, digite um número inteiro válido.\33[38m')
            continue
        else:
            return n

def cabeçalho(msg):
    print('-=-' * 25)
    print(msg.center(75))
    print('-=-' * 25)


def menu(lista):
    cabeçalho('GERADOR DE SENHAS')
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    print('-' * 75)
    opc = leiaint('Sua opção: ')
    return opc
