# historico_gui.py - UI de histórico e edição

import csv
from tkinter import Toplevel, Label, Entry, Button
from tkinter import messagebox
from tkinter import ttk
from gerdor_gui.eventos_gui import ler_historico
from gerdor_gui.constantes_gui import ARQUIVO_HISTORICO, BG_PRINCIPAL, BTN_BG_GERAR, BTN_FG_PADRAO

def abrir_janela_historico(janela_root):
    """
    Abre uma nova janela (Toplevel) que exibe o histórico de senhas salvas
    em formato tabular (Treeview) com as colunas: data/hora, senha e local.
    Permite editar a coluna 'local' via duplo clique, salvando as alterações no CSV.
    """
    dados = ler_historico()
    if not dados:
        messagebox.showinfo("Histórico", "Nenhuma senha foi salva ainda.")
        return
    
    # Cria a nova janela de histórico
    topo = Toplevel(janela_root)
    topo.title("Histórico de Senhas")
    topo.geometry("600x400")
    topo.configure(bg=BG_PRINCIPAL)

    Label(topo, text="Histórico de Senhas Salvas",
          font=("Helvetica", 13, "bold"), bg=BG_PRINCIPAL).pack(pady=10)
    
    # Cria o Treeview com as colunas: data, senha e local
    cols = ("data", "senha", "local")
    tree = ttk.Treeview(topo, columns=cols, show="headings")
    for col, w, txt in [("data", 150, "Data/Hora"),
                        ("senha", 250, "Senha"),
                        ("local", 150, "Local")]:
        tree.heading(col, text=txt)
        tree.column(col, width=w)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Inserir registros
    for row in dados:
        tree.insert("", "end", values=(row["data"], row["senha"], row["local"]))

    def salvar_csv():
        """Regrava o CSV com os dados atuais da Treeview."""
        items = tree.get_children()
        with open(ARQUIVO_HISTORICO, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=cols)  # type: ignore
            writer.writeheader()
            for item in items:
                vals = tree.item(item, "values")
                writer.writerow({"data": vals[0], "senha": vals[1], "local": vals[2]})

    # Adicionar local onde a senha será utilizada
    def on_duplo_clique(event):
        """
        Permite editar apenas a coluna 'local' (terceira coluna).
        Salva ao pressionar Enter.
        """
        item = tree.focus()
        coluna = tree.identify_column(event.x)
        if coluna != "#3":  # somente coluna 'local'
            return

        x, y, w, h = tree.bbox(item, coluna)
        abs_x = tree.winfo_rootx() + x
        abs_y = tree.winfo_rooty() + y

        entry = Entry(topo)
        entry.place(x=abs_x, y=abs_y, width=w, height=h)
        entry.insert(0, tree.item(item, "values")[2])
        entry.focus_set()

        def salvar(_=None):
            nova = entry.get()
            vals = list(tree.item(item, "values"))
            vals[2] = nova
            tree.item(item, values=vals)
            entry.destroy()
            salvar_csv()

        entry.bind("<Return>", salvar)
        entry.bind("<FocusOut>", lambda e: entry.destroy())

    tree.bind("<Double-1>", on_duplo_clique)

    # Status bar (tooltip)
    def mostrar_tooltip(msg, timeout=2000):
        """Exibe msg no status e limpa após timeout (ms)."""
        status.config(text=msg)
        topo.after(timeout, lambda: status.config(text=""))

    # Permite copiar uma senha já salva no histórico
    def copiar_senha(event):
        """
        Copia a senha do item clicado com o botão direito para a área de transferência.
        """
        item_id = tree.identify_row(event.y)
        if not item_id:
            return
        senha = tree.item(item_id, "values")[1]  # índice 1 = coluna "senha"
        topo.clipboard_clear()
        topo.clipboard_append(senha)
        mostrar_tooltip("Senha copiada para a área de transferência!")
       
    tree.bind("<Button-3>", copiar_senha)  # Clique direito do mouse

    Button(topo, text="Fechar", command=topo.destroy,
           bg=BTN_BG_GERAR, fg=BTN_FG_PADRAO,
           font=("Helvetica", 10, "bold")).pack(pady=10)
