# 🔐 Gerador de Senhas Interativo & GUI 
Uma ferramenta em Python para criar senhas seguras de duas formas:
- CLI (linha de comando) – rápida e leve.
- GUI (interface gráfica) – intuitiva e rica em recursos.

## 📖 Descrição
Este projeto oferece geração de senhas robustas, com parâmetros de customização de comprimento e tipos de caracteres. Ele registra automaticamente cada senha gerada, permitindo consulta, edição de metadados (campo “local”) e cópia direta do histórico — tudo em uma única aplicação modular.

## 🚀 Funcionalidades
### Comum (CLI + GUI)
- Comprimento personalizável (mínimo de 6 caracteres).
- Inclusão/exclusão de:
  - Letras maiúsculas
  - Letras minúsculas
  - Dígitos numéricos
  - Caracteres especiais
  - Geração de múltiplas senhas de uma vez.
  - Salvamento automático no histórico (.csv no GUI, .txt no CLI).
  - Tratamento robusto de erros e validação de entradas.
    
### CLI
- Menu de texto interativo.
- Geração de “super-senhas” com critérios de alta complexidade.
- Saída em múltiplos formatos: terminal e arquivo .txt.
- Suporte a flags (ex.: --length, --count, --no-special).
  
### GUI
- Interface moderna com Tkinter.
- Checkbox para tipos de caracteres.
- Árvore interativa (Treeview) para exibir histórico:
- Edição inline da coluna Local com duplo clique.
- Cópia de uma senha para o clipboard via clique direito.
- Tooltip suave de confirmação de cópia.
- Barra de status dinâmica.

## 🛠️ Tecnologias e Ferramentas
- Python 3.8+
- Tkinter (GUI nativa)
- Módulos internos (lib/funcoes.py)
- CSV e manipulação de arquivos
- Git & GitHub para versionamento

## 📦 Estrutura do Projeto
```
gerador_senhas/
├── LICENSE
├── README.md
├── main_gui.py               # Ponto de entrada da GUI
├── gerador_senhas_cli.py     # Ponto de entrada da CLI                                                 
├── gerador_gui/
│   ├── constantes.py         # Cores, dimensões e nomes de arquivos
│   ├── eventos.py            # Lógica de geração, cópia e leitura de histórico
│   ├── historico.py          # Toplevel do histórico com Treeview editável
│   └── interface_gui.py      # Montagem da janela e widgets Tkinter
├── gerador_cli/
│    └── interface_cli.py     # Menu e fluxo da versão CLI
├── lib/
│   ├── funcoes.py            # Geração de senha e gravação em arquivo
│   └── __init__.py           
└── requirements.txt          # Dependências
```

## 🚀 Como Executar
### Pré-requisitos
- Python 3.8 ou superior instalado
- (Opcional) Crie um ambiente virtual:
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
pip install -r requirements.txt

#### 🖥️ Modo CLI
- Navegue até a pasta do projeto:
cd gerador_senhas
- Execute o script do CLI:
python gerador_senhas_cli.py
- Siga as instruções no terminal:
  - Informe o comprimento desejado.
  - Escolha tipos de caracteres.
  - Opcional: número de senhas a gerar.
  - Opcional: flags de configuração rápida.
#### 🖱️ Modo GUI
- Certifique-se de ter o diretório lib/ com funcoes.py.
- No terminal:
python main_gui.py
- A interface aparecerá:
  - Marque as opções de caracteres.
  - Defina quantidade e comprimento.
  - Clique em Gerar Senha.
  - Utilize Copiar (GUI) ou clique direito (Histórico) para copiar.

## 📂 Exemplos de Uso
### CLI
$ python interface_cli.py --length 12 --count 3 --no-special
- Gerando 3 senhas de 12 caracteres (sem especiais)…
1) aB3dE4fG5hI2
2) JkL9mN8oP7qR
3) StU6vW5xY4zA
Senhas salvas em geradas.txt

![Menu_interativo](https://github.com/user-attachments/assets/c3fde19d-ab9c-4a51-91d2-a3e33289b748)
![saida_senhas](https://github.com/user-attachments/assets/12c4c4d5-6c64-4682-8130-1ffff366d7f3) 
![historico_senhas](https://github.com/user-attachments/assets/1e89c514-9f4a-4f2c-9719-ccdcbdc61057)

### GUI
![Captura de tela 2025-06-26 132745](https://github.com/user-attachments/assets/d67b5a43-4a0f-48ef-925a-a9fd180dfc5f)
![Captura de tela 2025-06-26 132933](https://github.com/user-attachments/assets/beb72207-a3c5-4024-a73d-c8157a340a74)
- Duplo clique na coluna Local para editar.
- Clique direito em qualquer linha para copiar a senha com tooltip confirmando.

📝 Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

🙋‍♂️ Autor
Felipe Leal
- GitHub: @FelipeLeal92
- Email: fmatheus1992@gmail.com
Sinta-se à vontade para abrir issues, enviar pull requests e sugerir melhorias!


