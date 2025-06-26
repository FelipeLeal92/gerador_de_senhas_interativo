# eventos_gui.py - lógica de geração, cópia e leitura de histórico.

import os
import csv
from tkinter import messagebox
from lib.funcoes import gerador_senha, salvar_senha
from gerdor_gui.constantes_gui import ARQUIVO_HISTORICO

# Função chamada quando o botão "Gerar Senha(s)" é pressionado
def gerar_senhas(form_widgets):
    """
    Valida entradas do usuário, gera lista de senhas e grava no CSV.
    Retorna lista de senhas ou None em caso de erro.
    form_widgets: dict com referências a Entry/BooleanVar/Text.
    """
    # 1) Validar tamanho
    try:
        tamanho = int(form_widgets["entrada_digitos"].get())
        if tamanho < 6:
            raise ValueError("A senha deve ter ao menos 6 caracteres.")
    except ValueError as err:
        messagebox.showerror("Valor Inválido", str(err))
        return None

    # 2) Validar seleção de tipos de caracteres
    if not any([
        form_widgets["use_minusculas"].get(),
        form_widgets["use_maiusculas"].get(),
        form_widgets["use_digitos"].get(),
        form_widgets["use_especiais"].get()
    ]):
        messagebox.showerror("Seleção Necessária",
                             "Selecione ao menos um tipo de caractere.")
        return None

    # 3) Quantidade de senhas a gerar
    qtd_text = form_widgets["entrada_qtd"].get().strip()
    try:
        qtd = int(qtd_text) if qtd_text else 1
    except ValueError:
        qtd = 1

    # 4) Gerar senhas e salvar
    senhas = []
    for _ in range(qtd):
        senha = gerador_senha(
            tamanho,
            use_minusculas=form_widgets["use_minusculas"].get(),
            use_maiusculas=form_widgets["use_maiusculas"].get(),
            use_digitos=form_widgets["use_digitos"].get(),
            use_especiais=form_widgets["use_especiais"].get()
        )
        if senha is None:
            messagebox.showerror("Erro Interno",
                                 "Não foi possível gerar a senha.")
            return None
        senhas.append(senha)
        salvar_senha(senha)

    return senhas

# Atualiza a caixa de texto com uma senha por linha
def atualizar_caixa_senhas(caixa, senhas):
    """
    Exibe a lista de senhas na Text widget.
    caixa: Text widget; senhas: lista de strings.
    """
    caixa.config(state="normal")
    caixa.delete("1.0", "end")
    for senha in senhas:
        caixa.insert("end", senha + "\n")
    caixa.config(state="disabled")

# Função para copiar a senha gerada
def copiar_para_clipboard(janela, caixa):
    """
    Copia todo o texto da caixa de senhas para o clipboard do sistema.
    """
    conteudo = caixa.get("1.0", "end").strip()
    if not conteudo:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar!")
        return
    janela.clipboard_clear()
    janela.clipboard_append(conteudo)
    messagebox.showinfo("Copiado", "Senha(s) copiadas para a área de transferência!")

def ler_historico():
    """
    Lê o CSV de histórico e retorna lista de dicts: {"data", "senha", "local"}.
    """
    if not os.path.exists(ARQUIVO_HISTORICO):
        return []
    with open(ARQUIVO_HISTORICO, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]