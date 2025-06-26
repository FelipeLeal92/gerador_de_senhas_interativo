# main_gui.py - inicia o loop principal.

from gerdor_gui.interface_gui import criar_interface

def main():
    janela = criar_interface()
    janela.mainloop()

if __name__ == "__main__":
    main()