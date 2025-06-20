#main_gui
from tkinter import *
from tkinter import ttk, messagebox 
from lib.funcoes import gerador_senha, salvar_senha # Funções já existentes
import os, csv


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

    # Atualiza a caixa de texto com uma senha por linha
    caixa_senhas.config(state="normal")
    caixa_senhas.delete("1.0", END)
    for senha in senhas:
        caixa_senhas.insert(END, senha + "\n")
    caixa_senhas.config(state="disabled")

    # Salva as senhas geradas em um arquivo.
    for senha in senhas:
        salvar_senha(senha)


def copiar_para_clipboard():
    senha = caixa_senhas.get("1.0", END).strip()
    if senha.strip() == "":
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar!")
        return
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")


def abrir_janela_historico():
    """
    Abre uma nova janela (Toplevel) que exibe o histórico de senhas salvas
    em formato tabular (Treeview) com as colunas: data/hora, senha e local.
    Permite editar a coluna 'local' via duplo clique, salvando as alterações no CSV.
    """
    filename = "senhas_salvas.csv"  # Certifique-se de usar o mesmo arquivo definido em salvar_senha.
    if not os.path.exists(filename):
        messagebox.showinfo("Histórico", "Nenhuma senha foi salva ainda.")
        return

    # Carrega os dados do CSV
    dados = []
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dados.append(row)

    # Cria a nova janela de histórico
    janela_historico = Toplevel(janela)
    janela_historico.title("Histórico de Senhas")
    janela_historico.geometry("600x400")
    janela_historico.configure(bg="white")

    Label(janela_historico, text="Histórico de Senhas Salvas",
          font=("Helvetica", 13, "bold"), bg="white", fg="#333").pack(pady=10)

    # Cria o Treeview com as colunas: data, senha e local
    colunas = ("data", "senha", "local")
    tree = ttk.Treeview(janela_historico, columns=colunas, show="headings")
    tree.heading("data", text="Data/Hora")
    tree.heading("senha", text="Senha")
    tree.heading("local", text="Local")
    tree.column("data", width=150)
    tree.column("senha", width=250)
    tree.column("local", width=150)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Insere os dados carregados no Treeview
    for row in dados:
        tree.insert("", "end", values=(row["data"], row["senha"], row["local"]))

    def atualizar_csv():
        """Percorre todos os itens do Treeview e regrava o arquivo CSV com os dados atualizados."""
        all_items = tree.get_children()
        with open(filename, "w", newline="", encoding="utf-8") as a:
            nomes_colunas = ["data", "senha", "local"]
            writer = csv.DictWriter(a, fieldnames=nomes_colunas) # type: ignore
            writer.writeheader()
            for item in all_items:
                values = tree.item(item, "values")
                writer.writerow({"data": values[0], "senha": values[1], "local": values[2]})

    def on_double_click(event):
        """
        Permite a edição da célula na coluna 'local' ao dar duplo clique na respectiva célula.
        Ao pressionar Enter, a edição é salva e o CSV é atualizado.
        """
        item_id = tree.focus()
        column = tree.identify_column(event.x)
        # Permite edição somente na terceira coluna ("local" – identificada como "#3")
        if column == "#3":
            x, y, width, height = tree.bbox(item_id, column)
            abs_x = tree.winfo_rootx() + x
            abs_y = tree.winfo_rooty() + y

            entry_edit = Entry(janela_historico)
            entry_edit.place(x=abs_x, y=abs_y, width=width, height=height)
            current_value = tree.item(item_id, "values")[2]
            entry_edit.insert(0, current_value)
            entry_edit.focus_set()

            def salvar_edicao(_):
                new_value = entry_edit.get()
                values = list(tree.item(item_id, "values"))
                values[2] = new_value
                tree.item(item_id, values=values)
                entry_edit.destroy()
                atualizar_csv()

            entry_edit.bind("<Return>", salvar_edicao)
            entry_edit.bind("<FocusOut>", lambda e: entry_edit.destroy())

    tree.bind("<Double-1>", on_double_click)

    Button(janela_historico, text="Fechar", command=janela_historico.destroy,
           bg="#4caf50", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)



# Régua invisíel
ESPACO_X = 20  # Margem horizontal consistente
ESPACO_Y = 10  # Espaço vertical entre elementos
ESPACO_ENTRE_SECOES = 25  # Espaço maior entre blocos

# Criando a janela principal
janela = Tk()
janela.title("Gerador de Senhas")
janela.configure(bg='white')
janela.geometry('500x800')

# Título do aplicativo
titulo = Label(janela, text="Gerador de Senhas", font=("Helvetica", 16, "bold"), fg="#333", bg="white")
titulo.pack(pady=ESPACO_ENTRE_SECOES)

#Criando Frame das opções de caracteres
frame_opc = LabelFrame(janela, text="Opções de caracteres", padx=8, pady=8, bg="white", font=("Helvetica", 12, "bold"), fg="#555")
frame_opc.pack(padx=ESPACO_X, pady=ESPACO_Y, fill='both', expand=True)

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
frame_tam.pack(pady=ESPACO_ENTRE_SECOES)

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
entrada_digitos.insert(0, "6")

# Botão para gerar a senha
botao_gerar = Button(janela, text="Gerar Senha", command=clicar_gerar, bg="#2196f3", fg="white", font=("Helvetica", 10, "bold"))
botao_gerar.pack(padx=ESPACO_X)

# Frame para exibir a senha gerada
frame_exibir = Frame(janela, bg="white")
frame_exibir.pack(pady=ESPACO_ENTRE_SECOES)

Label(frame_exibir, text="Senha(s) Gerada(s): ", bg="white", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=ESPACO_X)

# Frame interno para Text + Scrollbar
scroll_frame = Frame(frame_exibir, bg="white")
scroll_frame.pack()

scrollbar = Scrollbar(scroll_frame)
scrollbar.pack(side=RIGHT, fill=Y)

caixa_senhas = Text(scroll_frame, width=70, height=6, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
caixa_senhas.pack(side=LEFT, padx=ESPACO_X)

scrollbar.config(command=caixa_senhas.yview)
caixa_senhas.config(state="disabled")

# Botão para copiar
Button(frame_exibir, text="Copiar Senha(s)", command=copiar_para_clipboard, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold")).pack(pady=(10, 4))
# Botão de histórico
Button(frame_exibir, text="Ver histórico de senhas", command=abrir_janela_historico,
       bg="#ff9800", fg="white", font=("Helvetica", 10, "bold")).pack(pady=(0, 10))

#mainloop - Looping infinito, permanece com a janela aberta
janela.mainloop()
