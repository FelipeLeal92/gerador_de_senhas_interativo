# gui_interface.py - monta a janela, cria widgets e vincula funções

import tkinter as tk
from tkinter import BooleanVar, Scrollbar, Text, RIGHT, Y, END, Label, Frame, Button, Entry, Checkbutton, LabelFrame
from gerdor_gui.constantes_gui import (
    BG_PRINCIPAL, FG_TITULO, BTN_BG_GERAR, BTN_FG_PADRAO,
    BTN_BG_COPIAR, BTN_BG_HIST, ESPACO_X, ESPACO_Y, ESPACO_ENTRE_SECOES,
    JANELA_LARGURA, JANELA_ALTURA
)
from gerdor_gui.eventos_gui import (
    gerar_senhas, atualizar_caixa_senhas, copiar_para_clipboard
)
from gerdor_gui.historico_gui import abrir_janela_historico

def criar_interface():
    # janela principal
    janela = tk.Tk()
    janela.title("Gerador de Senhas")
    janela.configure(bg=BG_PRINCIPAL)
    janela.geometry(f"{JANELA_LARGURA}x{JANELA_ALTURA}")

    # título
    Label(janela, text="Gerador de Senhas",
          font=("Helvetica", 16, "bold"),
          fg=FG_TITULO, bg=BG_PRINCIPAL).pack(
        pady=ESPACO_ENTRE_SECOES)

    # frame de opções de caracteres
    frame_opc = LabelFrame(janela, text="Opções de caracteres",
                           padx=8, pady=8,
                           bg=BG_PRINCIPAL,
                           font=("Helvetica", 12, "bold"),
                           fg="#555")
    frame_opc.pack(padx=ESPACO_X, pady=ESPACO_Y, fill='both', expand=True)

    # variáveis associadas aos checkbuttons
    use_maiusculas = BooleanVar()
    use_minusculas = BooleanVar()
    use_digitos    = BooleanVar()
    use_especiais  = BooleanVar()

    for texto, var in [
        ("Letras Maiúsculas", use_maiusculas),
        ("Letras Minúsculas", use_minusculas),
        ("Valor Numérico", var:=use_digitos),
        ("Caracteres Especiais", use_especiais)
    ]:
        Checkbutton(frame_opc, text=texto, variable=var,
                    bg=BG_PRINCIPAL,
                    font=("Helvetica", 11)).pack(
            anchor="w", pady=4)

    # frame para quantidades e tamanho
    frame_tam = Frame(janela, bg=BG_PRINCIPAL)
    frame_tam.pack(pady=ESPACO_ENTRE_SECOES)

    # quantidade de senhas
    linha1 = Frame(frame_tam, bg=BG_PRINCIPAL)
    linha1.pack(anchor="w", padx=ESPACO_X, pady=ESPACO_Y)
    Label(linha1, text="Quantidade de Senhas:",
          bg=BG_PRINCIPAL, font=("Helvetica", 10)).pack(side="left")
    entrada_qtd = Entry(linha1, width=5, font=("Helvetica", 10))
    entrada_qtd.pack(side="left", padx=5)
    entrada_qtd.insert(0, "1")

    # comprimento da senha
    linha2 = Frame(frame_tam, bg=BG_PRINCIPAL)
    linha2.pack(anchor="w", padx=ESPACO_X, pady=ESPACO_Y)
    Label(linha2, text="Comprimento da Senha:",
          bg=BG_PRINCIPAL, font=("Helvetica", 10)).pack(side="left")
    entrada_digitos = Entry(linha2, width=5, font=("Helvetica", 10))
    entrada_digitos.pack(side="left", padx=5)
    entrada_digitos.insert(0, "6")

    # caixa de exibição de senhas
    frame_exibir = Frame(janela, bg=BG_PRINCIPAL)
    frame_exibir.pack(pady=ESPACO_ENTRE_SECOES)
    Label(frame_exibir, text="Senha(s) Gerada(s):",
          bg=BG_PRINCIPAL, font=("Helvetica", 11, "bold")).pack(
        anchor="w", padx=ESPACO_X)

    scroll_frame = Frame(frame_exibir, bg=BG_PRINCIPAL)
    scroll_frame.pack()
    scrollbar = Scrollbar(scroll_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    caixa_senhas = Text(scroll_frame, width=70, height=6,
                        font=("Helvetica", 12),
                        yscrollcommand=scrollbar.set)
    caixa_senhas.pack(side="left", padx=ESPACO_X)
    caixa_senhas.config(state="disabled")
    scrollbar.config(command=caixa_senhas.yview)

    # botões de ação
    btn_gerar = Button(frame_tam, text="Gerar Senha",
                       bg=BTN_BG_GERAR, fg=BTN_FG_PADRAO,
                       font=("Helvetica", 10, "bold"))
    btn_gerar.pack(padx=ESPACO_X)

    btn_copiar = Button(frame_exibir, text="Copiar Senha(s)",
                        bg=BTN_BG_COPIAR, fg=BTN_FG_PADRAO,
                        font=("Helvetica", 10, "bold"))
    btn_copiar.pack(pady=(10, 4))

    btn_hist = Button(frame_exibir, text="Ver histórico de senhas",
                      bg=BTN_BG_HIST, fg=BTN_FG_PADRAO,
                      font=("Helvetica", 10, "bold"))
    btn_hist.pack(pady=(0, 10))

    # dicionário de widgets/vars para passar aos handlers
    form_widgets = {
        "use_maiusculas": use_maiusculas,
        "use_minusculas": use_minusculas,
        "use_digitos":    use_digitos,
        "use_especiais":  use_especiais,
        "entrada_qtd":    entrada_qtd,
        "entrada_digitos":entrada_digitos
    }

    # vincular eventos
    btn_gerar.config(
        command=lambda: _on_gerar(form_widgets, caixa_senhas)
    )
    btn_copiar.config(
        command=lambda: copiar_para_clipboard(janela, caixa_senhas)
    )
    btn_hist.config(
        command=lambda: abrir_janela_historico(janela)
    )

    # dispara a janela
    return janela

def _on_gerar(form_widgets, caixa_senhas):
    """Chamado ao clicar em Gerar: gera e exibe senhas."""
    senhas = gerar_senhas(form_widgets)
    if senhas:
        atualizar_caixa_senhas(caixa_senhas, senhas)