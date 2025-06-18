#main_gui
from tkinter import *
from tkinter import ttk, messagebox 
from lib.funcoes import gerador_senha, comprimento, salvar_senha # Funções já existentes

# Função chamada quando o botão "Gerar Senha(s)" é pressionado.
def clicar_gerar():
    try:
        tamanho = int(entrada_digitos.get())
    except ValueError:
        messagebox.showerror("Valor Inválido", "Insira um número válido para o tamanho.")
        return

    if tamanho < 6:
        messagebox.showwarning("Aviso", "A senha deve conter no MÍNIMO 6 caracteres.")
        return
    
    # Verifica se pelo menos uma opção foi marcada
    if not (use_minusculas.get() or use_maiusculas.get() or use_digitos.get() or use_especiais.get()):
        messagebox.showerror("Seleção necessária", "Selecione pelo menos uma categoria de caracteres.")
        return

    # Obtém a quantidade de senhas solicitadas. Se não informado, gera uma.
    qtd_text = entrada_qtd.get()
    try:
        qtd = int(qtd_text) if qtd_text.strip() != "" else 1
    except ValueError:
        qtd = 1

    senhas = []
    for _ in range(qtd):
        senha = gerador_senha(
            tamanho,
                                use_minusculas=use_minusculas.get(),
                                use_maiusculas=use_maiusculas.get(),
                                use_digitos=use_digitos.get(),
                                use_especiais=use_especiais.get()
        )
        # Se ocorrer o erro de não ter nenhum caractere selecionado.
        if senha is None:
            messagebox.showerror("Seleção Necessária", "Selecione pelo menos uma categoria de caracteres.")
            return
        senhas.append(senha)

    # Exibe as senhas geradas na mesma caixa, separadas por vírgula.
    senhas_str = ", ".join(senhas)
    entrada_senha.config(state=NORMAL)
    entrada_senha.delete(0, END)
    entrada_senha.insert(0, senhas_str)
    entrada_senha.config(state="readonly")

    # Salva as senhas geradas em um arquivo.
    for senha in senhas:
        salvar_senha(senha)


def copiar_para_clipboard():
    senha = entrada_senha.get()
    if senha.strip() == "":
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar!")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")

# Régua invisíel
ESPACO_X = 20  # Margem horizontal consistente
ESPACO_Y = 10  # Espaço vertical entre elementos
ESPACO_ENTRE_SECOES = 25  # Espaço maior entre blocos

# Criando a janela principal
janela = Tk()
janela.title("Gerador de Senhas")
janela.configure(bg='white')
janela.geometry('500x700')

# Título do aplicativo
titulo = Label(janela, text="Gerador de Senhas", font=("Helvetica", 16, "bold"), fg="#333", bg="white")
titulo.pack(pady=ESPACO_ENTRE_SECOES)

#Criando Frame das opções de caracteres
frame_opc = LabelFrame(janela, text="Opções de caracteres", padx=8, pady=8, bg="white", font=("Helvetica", 12, "bold"), fg="#555")
frame_opc.pack(padx=ESPACO_X, pady=ESPACO_Y, fill='both', expand='yes')

#Criando variáveis para armazenar as seleções
use_maiusculas = BooleanVar()
use_minusculas = BooleanVar()
use_digitos = BooleanVar()
use_especiais = BooleanVar()

#Criando Fame com Checkbuttons para escolher as opções de caracteres
Checkbutton(frame_opc, text='Letras Maiúsculas', variable = use_maiusculas, bg='white', font=("Helvetica", 11)).pack(anchor="w", pady=4)
Checkbutton(frame_opc, text='Letras Minúsculas', variable = use_minusculas, bg='white', font=("Helvetica", 11)).pack(anchor="w", pady=4)
Checkbutton(frame_opc, text='Valor Numérico', variable = use_digitos, bg='white', font=("Helvetica", 11)).pack(anchor="w", pady=4)
Checkbutton(frame_opc, text='Caracteres especiais', variable = use_especiais, bg='white', font=("Helvetica", 11)).pack(anchor="w", pady=4)                     

# Frame para definir a quantidade de senhas e comprimento da senha
frame_tam = Frame(janela, bg="white")
frame_tam = Frame(janela, bg="white").pack(pady=ESPACO_ENTRE_SECOES)

# Quantidade de senhas
linha1 = Frame(frame_tam, bg="white")
linha1.pack(anchor="w", padx=ESPACO_X, pady=ESPACO_Y)
Label(linha1, text="Quantidade de Senhas:", bg="white", font=("Helvetica", 10)).pack(side="left")
entrada_qtd = Entry(linha1, width=5, font=("Helvetica", 10))
entrada_qtd.pack(side="left", padx=5)
entrada_qtd.insert(0, "1")  # Valor padrão

# Comprimento das senhas
linha2 = Frame(frame_tam, bg="white")
linha2.pack(anchor="w", padx=ESPACO_X, pady=ESPACO_Y)
Label(linha2, text="Comprimento da Senha:", bg="white", font=("Helvetica", 10)).pack(side="left")
entrada_digitos = Entry(linha2, width=5, font=("Helvetica", 10))
entrada_digitos.pack(side="left", padx=5)
entrada_digitos.insert(0, 6)

# Botão para gerar a senha
botao_gerar = Button(janela, text="Gerar Senha", command=clicar_gerar, bg="#2196f3", fg="white", font=("Helvetica", 10, "bold"))
botao_gerar.pack(padx=ESPACO_X)

# Frame para exibir a senha gerada
frame_exibir = Frame(janela, bg="white")
frame_exibir.pack(pady=ESPACO_ENTRE_SECOES)

Label(frame_exibir, text="Senha(s) Gerada(s): ", bg="white", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=ESPACO_X)
entrada_senha = Entry(frame_exibir, width=70, font=("Helvetica", 12))
entrada_senha.pack(side='left', padx=ESPACO_X, ipady=6)
entrada_senha.config(state="readonly")

# Botão para copiar
botao_copiar = Button(janela, text="Copiar Senha(s)", command=copiar_para_clipboard, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"))
botao_copiar.pack(pady=10)

#mainloop - Looping infinito, permanece com a janela aberta
janela.mainloop()
