from gerador_senhas.lib.funções import *
from gerador_senhas.lib.interface import *
from time import sleep

arq = 'senhas_geradas.txt'

while True:
    resposta = menu(['Criar uma senha (mínimo 6 caracteres)', 'Criar mais de uma senha (mínimo 6 caracteres)',
                     'Super-senha (mínimo de 16 dígitos e todos os caracteres inclusos', 'Sair'])

    if resposta == 1:   #Opção para criar uma única senha
        tamanho = comprimento()
        minusculas, maiusculas, digitos, especiais = caracteres()
        senha = opc1(tamanho, minusculas, maiusculas, digitos, especiais)
        print('Senha gerada: ', senha)
        CriarCadastrar(arq, [senha])
        sleep(2)

    elif resposta == 2:   #Opção para criar mais de uma senha
        senhas = opc2()
        CriarCadastrar(arq, senhas)
        sleep(2)

    elif resposta == 3:   # Opção para criar super-senha
        senha = opc1(tamanho=16, minusculas=True, maiusculas=True, digitos=True, especiais=True)
        CriarCadastrar(arq, [senha])
        print('Senha gerada: ', senha)
        sleep(2)

    elif resposta == 4:
        print('Obrigado por usar o gerador de senhas, volte sempre!')
        break
    else:
        print('\33[31mDigite um valor válido!\33[m')
        sleep(1)
